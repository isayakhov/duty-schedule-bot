import logging
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

DAYS_OF_DUTY = int(os.getenv("DAYS_OF_DUTY", "5"))

PLATFORM = str(os.getenv("PLATFORM", "telegram"))

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
