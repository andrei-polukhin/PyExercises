import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s \
    [%(filename)s:%(lineno)d] %(message)s",
    level=logging.INFO,
    filename="logs.txt"
)
logger = logging.getLogger(__name__)

logger.info("Hello, I\'m just to inform you: you are cool!")
logger.debug("Hi")
logger.critical("OOOPS")
