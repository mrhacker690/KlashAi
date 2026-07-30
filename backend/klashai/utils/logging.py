import logging
import sys

from klashai.config import settings


def setup_logging():
    """Configure logging for the application."""
    level = logging.DEBUG if settings.environment == "development" else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
