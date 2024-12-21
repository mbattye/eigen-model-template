import logging

def setup_logger(log_level="INFO"):
    """
    Configure the logger.
    """
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=getattr(logging, log_level.upper(), logging.INFO)
    )
    return logging.getLogger("eigen-model-template")
