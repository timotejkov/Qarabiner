"""
Behave environment hooks for the Qarabiner BDD test suite.

Handles setup and teardown for test scenarios, including:
- Feature-level initialization
- Scenario-level cleanup
- Context management
- Logging configuration
"""

import logging
import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


# Configure logging for tests
def setup_logging():
    """Configure logging for BDD tests."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )
    # Suppress verbose logs from certain modules
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)


# ============================================================================
# Hooks
# ============================================================================

def before_all(context):
    """
    Run before all features are executed.

    Sets up test environment, loads configuration, initializes shared resources.
    """
    setup_logging()
    logger = logging.getLogger("behave")
    logger.info("=" * 80)
    logger.info("Starting Qarabiner BDD Test Suite")
    logger.info("=" * 80)

    # Store logger in context for use in steps
    context.logger = logger

    # Initialize test configuration
    context.test_config = {
        "mock_llm": True,  # Use mock LLM by default for unit tests
        "live_api": False,  # Disabled unless @wip is used with API key
        "timeout": 30,  # Default timeout in seconds
    }

    logger.info("Test configuration: %s", context.test_config)


def after_all(context):
    """
    Run after all features are executed.

    Cleanup shared resources, print summary statistics.
    """
    logger = logging.getLogger("behave")
    logger.info("=" * 80)
    logger.info("Qarabiner BDD Test Suite Completed")
    logger.info("=" * 80)


def before_feature(context, feature):
    """
    Run before each feature is executed.

    Initialize feature-level context and resources.
    """
    logger = logging.getLogger("behave")
    logger.info(f"\nFeature: {feature.name}")
    logger.info("-" * 80)

    # Feature-level setup
    context.feature_name = feature.name
    context.scenario_count = 0


def after_feature(context, feature):
    """
    Run after each feature is executed.

    Cleanup feature-level resources.
    """
    logger = logging.getLogger("behave")
    logger.info(f"Feature completed: {context.scenario_count} scenarios executed")


def before_scenario(context, scenario):
    """
    Run before each scenario is executed.

    Initialize scenario-level context.
    """
    logger = logging.getLogger("behave")
    logger.info(f"  Scenario: {scenario.name}")

    # Increment scenario counter
    context.scenario_count = getattr(context, "scenario_count", 0) + 1

    # Initialize scenario-level attributes
    context.scenario_name = scenario.name
    context.scenario_start_time = None
    context.scenario_error = None

    # Check for tags that affect test behavior
    context.is_wip = "wip" in scenario.effective_tags
    context.is_slow = "slow" in scenario.effective_tags
    context.is_integration = "integration" in scenario.effective_tags

    # Log tags if any
    if scenario.effective_tags:
        logger.debug(f"    Tags: {', '.join(scenario.effective_tags)}")


def after_scenario(context, scenario):
    """
    Run after each scenario is executed.

    Cleanup scenario resources, log results.
    """
    logger = logging.getLogger("behave")

    if scenario.status == "passed":
        logger.info(f"    ✓ Passed")
    elif scenario.status == "failed":
        logger.error(f"    ✗ Failed")
        if hasattr(context, "scenario_error"):
            logger.error(f"      Error: {context.scenario_error}")
    elif scenario.status == "skipped":
        logger.warning(f"    ⊘ Skipped")

    # Cleanup scenario-specific resources
    cleanup_scenario_resources(context)


def before_step(context, step):
    """
    Run before each step is executed.
    """
    logger = logging.getLogger("behave")
    logger.debug(f"    Step: {step.name}")


def after_step(context, step):
    """
    Run after each step is executed.
    """
    if step.status == "failed":
        logger = logging.getLogger("behave")
        if step.exception:
            logger.error(f"      Exception: {step.exception}")


# ============================================================================
# Helper Functions
# ============================================================================

def cleanup_scenario_resources(context):
    """
    Clean up resources allocated during a scenario.

    Closes connections, clears temporary data, etc.
    """
    # Close HTTP clients if any
    if hasattr(context, "client") and hasattr(context.client, "close"):
        try:
            context.client.close()
        except Exception:
            pass

    # Close database connections if any
    if hasattr(context, "db_connection"):
        try:
            context.db_connection.close()
        except Exception:
            pass

    # Clear large data structures
    for attr in ["prd_text", "profile", "strategy", "validation", "result"]:
        if hasattr(context, attr):
            delattr(context, attr)


def get_test_data_path(filename: str) -> Path:
    """
    Get path to test data files.

    Args:
        filename: Name of test data file (e.g., "mattermost_prd.txt")

    Returns:
        Path to the test data file
    """
    test_data_dir = Path(__file__).parent / "test_data"
    return test_data_dir / filename


# ============================================================================
# Test Configuration Context Manager
# ============================================================================

class MockLLMContext:
    """Context manager for mock LLM testing."""

    def __init__(self, context):
        """Initialize with Behave context."""
        self.context = context
        self.original_config = None

    def __enter__(self):
        """Enable mock LLM mode."""
        self.context.test_config["mock_llm"] = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Restore original config."""
        pass


class LiveAPIContext:
    """Context manager for live API testing (requires API key)."""

    def __init__(self, context):
        """Initialize with Behave context."""
        self.context = context

    def __enter__(self):
        """Enable live API mode."""
        self.context.test_config["live_api"] = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Restore original config."""
        self.context.test_config["live_api"] = False


# ============================================================================
# Custom Assertion Helpers
# ============================================================================

def assert_field_present(obj, field_name: str, error_message: str = None):
    """
    Assert that an object has a field.

    Args:
        obj: Object to check
        field_name: Name of field
        error_message: Custom error message

    Raises:
        AssertionError if field is not present
    """
    if not hasattr(obj, field_name):
        msg = error_message or f"Field '{field_name}' not found in {type(obj).__name__}"
        raise AssertionError(msg)


def assert_field_value(obj, field_name: str, expected_value, error_message: str = None):
    """
    Assert that a field has a specific value.

    Args:
        obj: Object to check
        field_name: Name of field
        expected_value: Expected value
        error_message: Custom error message

    Raises:
        AssertionError if value doesn't match
    """
    actual_value = getattr(obj, field_name, None)
    if actual_value != expected_value:
        msg = error_message or \
            f"Field '{field_name}' expected '{expected_value}', got '{actual_value}'"
        raise AssertionError(msg)


def assert_collection_contains(collection, item, error_message: str = None):
    """
    Assert that a collection contains an item.

    Args:
        collection: Collection to check
        item: Item to find
        error_message: Custom error message

    Raises:
        AssertionError if item not found
    """
    if item not in collection:
        msg = error_message or f"Item '{item}' not found in collection"
        raise AssertionError(msg)


def assert_collection_non_empty(collection, error_message: str = None):
    """
    Assert that a collection is not empty.

    Args:
        collection: Collection to check
        error_message: Custom error message

    Raises:
        AssertionError if collection is empty
    """
    if not collection:
        msg = error_message or "Collection is empty"
        raise AssertionError(msg)


# ============================================================================
# Test Data Fixtures
# ============================================================================

SAMPLE_PRD_MINIMAL = """
A simple web application for team collaboration.
"""

SAMPLE_PRD_DETAILED = """
Platform Name: TeamHub

Architecture:
- Backend: Node.js 18 with Express framework
- Frontend: React 18 with TypeScript
- Database: PostgreSQL 13
- Cache: Redis 7
- Message Queue: RabbitMQ 3
- Infrastructure: Docker + Kubernetes on AWS ECS

Key Features:
1. User authentication with OAuth2
2. Real-time messaging via WebSocket
3. File upload and sharing
4. Search capabilities
5. Role-based access control

Security:
- TLS 1.2+ for all communications
- PII encryption at rest and in transit
- Regular security audits
- Compliance: GDPR, SOC 2

Performance Requirements:
- Target: < 200ms response time (95th percentile)
- Throughput: 10,000+ requests/second
- Availability: 99.95% uptime

Scale:
- Expected: 50,000+ concurrent users
- Peak load: 100,000 concurrent connections
"""

SAMPLE_PRD_MEDICAL = """
Medical Imaging Platform

Description:
A cloud-based medical imaging system for radiologists and clinicians.

Architecture:
- DICOM image processing backend in Python
- Web-based viewer frontend in React
- PostgreSQL for patient data
- HIPAA-compliant storage on AWS

Key Features:
- Upload and view DICOM images
- AI-assisted diagnosis
- Patient record management
- Secure sharing with providers

Regulatory:
- FDA clearance required
- HIPAA compliance mandatory
- IEC 62304 for medical device software
- ISO 13485 for quality management

Safety & Security:
- Patient data encryption
- Audit logging
- Access control per patient
- Backup and disaster recovery
"""

SAMPLE_PRD_AUTOMOTIVE = """
Automotive Infotainment System

Description:
In-vehicle entertainment and navigation system for passenger vehicles.

Technical:
- Embedded C++ software
- CAN bus integration
- Vehicle sensors (GPS, accelerometer, etc.)
- Touchscreen interface

Safety Requirements:
- ISO 26262 ASIL B compliance
- Fail-safe operation
- Emergency mode handling
- System diagnostics

Features:
- Navigation with real-time traffic
- Music and podcasts
- Vehicle diagnostics display
- Emergency call system
"""

# Make fixtures available to context
def add_sample_data_to_context(context):
    """Add sample PRD data to context."""
    context.sample_prds = {
        "minimal": SAMPLE_PRD_MINIMAL,
        "detailed": SAMPLE_PRD_DETAILED,
        "medical": SAMPLE_PRD_MEDICAL,
        "automotive": SAMPLE_PRD_AUTOMOTIVE,
    }
