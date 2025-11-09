import logging

# ساخت Logger
logger = logging.getLogger("AppLogger")
logger.setLevel(logging.INFO)

# ساخت فایل لاگ
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

# فرمت لاگ
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
