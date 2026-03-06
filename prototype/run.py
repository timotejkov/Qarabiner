#!/usr/bin/env python3
"""
Qarabiner — Entry Point

Starts the FastAPI server with the Qarabiner application.
Usage:
    ANTHROPIC_API_KEY=sk-ant-xxx python run.py

The web UI will be available at http://localhost:8000
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def main() -> None:
    """Validate environment and start the server."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY environment variable is required.")
        print("Usage: ANTHROPIC_API_KEY=sk-ant-xxx python run.py")
        sys.exit(1)

    import uvicorn
    print("\n🧗 Qarabiner — Test Strategy Engine")
    print("=" * 40)
    print(f"Starting server at http://localhost:8000")
    print(f"API docs at http://localhost:8000/docs")
    print("=" * 40 + "\n")
    uvicorn.run(
        "src.app:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info",
    )


if __name__ == "__main__":
    main()
