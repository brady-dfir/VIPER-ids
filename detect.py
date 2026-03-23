# Port scan, SYN flood, DNS detection

from datetime import datetime
from collections import defaultdict
from alert import format_alert
from logger import log_alert
from config import (
    PORT_SCAN_PORT_THRESHOLD, PORT_SCAN_TIME_WINDOW,
    SYN_FLOOD_SYN_THRESHOLD, SYN_FLOOD_TIME_WINDOW,
    SYN_FLOOD_MIN_SYN_ACK_RATIO,
    MAX_DOMAIN_LENGTH, MAX_SUBDOMAINS, SUSPICIOUS_TLDS,
    BLACKLIST_FILE
)

# Access blacklist
with open(BLACKLIST_FILE) as f:
    BLACKLIST = {line.strip() for line in f if line.strip()}

port_scan_data = defaultdict(lambda: {"ports": set(), "first_seen": datetime.now()})
syn_data = defaultdict(lambda: {"syn_times": [], "completed": 0})

def detect_malicious_ip(src, dst):
    if src in BLACKLIST:
        log_alert(format_alert("ALERT", f"Traffic from malicious IP {src} to {dst}"))
    if dst in BLACKLIST:
        log_alert(format_alert("ALERT", f"Traffic to malicious IP {dst} from {src}"))