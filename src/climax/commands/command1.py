from climax.utils import logutils

logger = logutils.get_logger(__name__)


def run():
    logger.info("This is an info message")
    logger.error("This is an error message")
    logger.warn("This is a warning message")
    logger.debug("This is a debug message")
