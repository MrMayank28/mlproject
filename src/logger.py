import logging
import os
from datetime import datetime


# # OLD CODE

# # Create the "logs" directory if it doesn't exist
# logs_directory = os.path.join(os.getcwd(), "logs")
# os.makedirs(logs_directory, exist_ok=True)

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

# OLD Code

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creates Logs file in the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# # To check whether the code is executing fine
# if __name__=="__main__":
#     logging.info("Logging has started")