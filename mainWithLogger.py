# --------------------------------------------------
# Author: ${USER}
# Date Created: ${DATE}
# --------------------------------------------------
"""
Module description goes here.
This module contains functions and classes related to ...
"""

# Imports
import asyncio
import logging
from datetime import datetime
import os

# Constants
LOGGING_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}


# Functions
def setup_logger(level='INFO', print_console=True, log_folder=None, log_to_file=True):
    script_name = os.path.basename(__file__).split('.')[0]

    logger = logging.getLogger()
    if print_console:
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)d] - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    if log_to_file:
        if log_folder is None:
            log_folder = os.path.join(os.path.dirname(__file__), f'logs_{script_name}')
        else:
            log_folder = os.path.join(log_folder, f'logs_{script_name}')

        os.makedirs(log_folder, exist_ok=True)

        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_filename = f"{script_name}_{current_time}.log"
        log_filepath = os.path.join(log_folder, log_filename)

        file_handler = logging.FileHandler(log_filepath)
        file_formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)d] - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    if level in LOGGING_LEVELS:
        logger.setLevel(LOGGING_LEVELS[level])
    else:
        logger.warning(f"Invalid logging level: {level}. Defaulting to INFO.")
        logger.setLevel(logging.INFO)

    if log_to_file:
        logger.info(f"Logs are being stored in: {log_folder}")

    return logger


# Logging
logger = setup_logger('DEBUG')


# Classes
class SampleClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        logger.info(f"Hello, {self.name}!")


# Main function
async def main():
    start_time = datetime.now()
    logger.info("Program started at: %s", start_time)

    # Your main code here

    sample_instance = SampleClass("World")
    sample_instance.greet()

    end_time = datetime.now()
    logger.info("Program ended at: %s", end_time)
    duration = end_time - start_time
    logger.info("Total time taken: %s", duration)


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())