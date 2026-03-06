"""
Standards Vector Store — semantic search using ChromaDB.

Provides embedding-based retrieval of standards sections as an upgrade
over keyword matching. Falls back gracefully if ChromaDB is not installed.

Uses ChromaDB's built-in default embedding function (all-MiniLM-L6-v2)
which runs locally — no external API calls needed for embeddings.
"""

import hashlib
import logging
from typing import Optional

logger = logging.getLogger(__name__)

try:
    import chromadb
    from chromadb.config import Settings
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False
    logger.warning("[VectorStore] chromadb not installed — falling back to keyword search")


class StandardsVectorStore:
    """
    ChromaDB-backed vector store for semantic search over standards.

    Usage:
        store = StandardsVectorStore()
        store.build_index(sections)  # list of StandardSection objects
        results = store.search("how to test for SQL injection", n=10)
    """

    def __init__(self, persist_dir: str = ".chroma_db") -> None:
        self._persist_dir = persist_dir
        self._collection = None
        self._initialized = False
        self._sections_by_id: dict[str, object] = {}

    @property
    def available(self) -> bool:
        """Check if ChromaDB is available and the index is built."""
        return CHROMADB_AVAILABLE and self._initialized

    def build_index(self, sections: list) -> None:
        """
        Build the semantic search index from all standard sections.

        Args:
            sections: List of StandardSection objects with standard_id,
                     section_key, title, content, and keywords fields.
        """
        if not CHROMADB_AVAILABLE:
            logger.info("[VectorStore] ChromaDB not available, skipping index build")
            return

        # Compute a hash of all section content to detect changes
        content_hash = hashlib.md5(
            "".join(s.content for s in sections).encode()
        ).hexdigest()[:12]

        try:
            client = chromadb.PersistentClient(
                path=self._persist_dir,
                settings=Settings(anonymized_telemetry=False),
            )

            collection_name = "standards_v1"

            # Check if collection exists and is up to date
            existing_collections = [c.name for c in client.list_collections()]
            if collection_name in existing_collections:
                existing = client.get_collection(collection_name)
                existing_meta = existing.metadata or {}
                if existing_meta.get("content_hash") == content_hash:
                    logger.info(f"[VectorStore] Index up to date ({len(sections)} sections, hash={content_hash})")
                    self._collection = existing
                    self._index_section_map(sections)
                    self._initialized = True
                    return
                else:
                    logger.info("[VectorStore] Standards content changed, rebuilding index...")
                    client.delete_collection(collection_name)

            # Build new collection
            self._collection = client.create_collection(
                name=collection_name,
                metadata={
                    "hnsw:space": "cosine",
                    "content_hash": content_hash,
                },
            )

            # Prepare documents for indexing
            ids = []
            documents = []
            metadatas = []

            for i, section in enumerate(sections):
                doc_id = f"sec_{i}"
                ids.append(doc_id)

                # Combine title + content + keywords for better embedding
                doc_text = (
                    f"{section.title}\n\n"
                    f"{section.content}\n\n"
                    f"Keywords: {', '.join(section.keywords)}"
                )
                documents.append(doc_text)

                # Store metadata for filtering and hierarchy
                meta = {
                    "standard_id": section.standard_id,
                    "section_key": section.section_key,
                    "title": section.title,
                    "keywords": ",".join(section.keywords),
                }

                # Add hierarchy fields if present (part, clause)
                if hasattr(section, "part") and section.part:
                    meta["part"] = section.part
                if hasattr(section, "clause") and section.clause:
                    meta["clause"] = section.clause

                metadatas.append(meta)

            # ChromaDB limits batch size to ~41666 due to embedding model constraints
            batch_size = 500
            for start in range(0, len(ids), batch_size):
                end = min(start + batch_size, len(ids))
                self._collection.add(
                    ids=ids[start:end],
                    documents=documents[start:end],
                    metadatas=metadatas[start:end],
                )

            self._index_section_map(sections)
            self._initialized = True
            logger.info(f"[VectorStore] Indexed {len(sections)} sections (hash={content_hash})")

        except Exception as e:
            logger.error(f"[VectorStore] Failed to build index: {e}")
            self._initialized = False

    def _index_section_map(self, sections: list) -> None:
        """Build a map from doc IDs to section objects for result retrieval."""
        self._sections_by_id = {f"sec_{i}": s for i, s in enumerate(sections)}

    def search(
        self,
        query: str,
        n: int = 15,
        standard_filter: Optional[str] = None,
    ) -> list:
        """
        Semantic search for relevant standard sections.

        Args:
            query: Natural language query (e.g., "how to test for SQL injection").
            n: Maximum number of results to return.
            standard_filter: Optional standard ID prefix to filter results
                           (e.g., "OWASP" to only search OWASP sections).

        Returns:
            List of StandardSection objects sorted by relevance.
        """
        if not self.available:
            return []

        try:
            where_filter = None
            if standard_filter:
                where_filter = {
                    "standard_id": {"$contains": standard_filter}
                }

            results = self._collection.query(
                query_texts=[query],
                n_results=min(n, self._collection.count()),
                where=where_filter,
            )

            # Map results back to StandardSection objects
            sections = []
            if results and results["ids"] and results["ids"][0]:
                for doc_id, distance in zip(results["ids"][0], results["distances"][0]):
                    section = self._sections_by_id.get(doc_id)
                    if section:
                        # Convert cosine distance to similarity score (0-1)
                        section.relevance_score = max(0, 1.0 - distance)
                        sections.append(section)

            return sections

        except Exception as e:
            logger.error(f"[VectorStore] Search failed: {e}")
            return []

    def search_by_hierarchy(
        self,
        standard_id: str,
        part: Optional[str] = None,
        clause: Optional[str] = None,
    ) -> list:
        """
        Retrieve sections by their position in the standards hierarchy.

        Args:
            standard_id: Standard identifier (e.g., "ISO/IEC/IEEE 29119").
            part: Optional part filter (e.g., "Part 2").
            clause: Optional clause filter (e.g., "6").

        Returns:
            List of matching StandardSection objects.
        """
        if not self.available:
            return []

        try:
            # Build where filter
            where_conditions = [
                {"standard_id": {"$contains": standard_id}}
            ]

            if part:
                where_conditions.append({"part": {"$eq": part}})
            if clause:
                where_conditions.append({"clause": {"$eq": clause}})

            where_filter = (
                {"$and": where_conditions}
                if len(where_conditions) > 1
                else where_conditions[0]
            )

            results = self._collection.get(
                where=where_filter,
                limit=50,
            )

            sections = []
            if results and results["ids"]:
                for doc_id in results["ids"]:
                    section = self._sections_by_id.get(doc_id)
                    if section:
                        sections.append(section)

            return sections

        except Exception as e:
            logger.error(f"[VectorStore] Hierarchy search failed: {e}")
            return []
