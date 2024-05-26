
import logging
import logging.config
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

logpath=os.path.join(os.getcwd(),"logs")

os.makedirs(logpath,exist_ok=True)

LOG_FILEPATH=os.path.join(logpath,LOG_FILE)
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)