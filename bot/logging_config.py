# bot/logging_config.py

import logging
import os
import argparse

os.makedirs(
    "logs",
    exist_ok=True
)

# Configure logging: console + file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/trading.log"),  # writes to logs/trading.log
        logging.StreamHandler()                   # prints to console
    ]
)
logger = logging.getLogger(__name__)


