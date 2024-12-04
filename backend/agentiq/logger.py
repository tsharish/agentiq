import logging

logger = logging.getLogger(__name__)
handler = logging.FileHandler("file.log")
handler.setLevel(logging.INFO)
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
