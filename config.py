# Settings and configurations

# Network Interface
INTERFACE = "eth0"

# Logging
LOG_FILE = "alerts.log"

# Port Scan Detection
PORT_SCAN_PORT_THRESHOLD = 20
PORT_SCAN_TIME_WINDOW = 60

# SYN Flood Detection
SYN_FLOOD_SYN_THRESHOLD = 100
SYN_FLOOD_TIME_WINDOW = 30
SYN_FLOOD_MIN_SYN_ACK_RATIO = 0.2

# DNS Detection
MAX_DOMAIN_LENGTH = 60
MAX_SUBDOMAINS = 5
SUSPICIOUS_TLDS = {".xyz", ".top", ".click", ".work", ".gq", ".tk"}

# Blacklist
BLACKLIST_FILE = "blacklist.txt"