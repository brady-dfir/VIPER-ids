# Saves alerts to LOG_FILE

from datetime import datetime
from config import LOG_FILE

def logAlert(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} [ALERT] {message}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")