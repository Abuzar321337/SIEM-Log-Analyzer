import os
import json
import time
from datetime import datetime
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200", request_timeout=30)

# Log file to read
log_file = "/var/log/syslog"

# Function to send logs to Elasticsearch
def send_to_elasticsearch(log_entry):
    try:
        es.index(index="syslog-python", document=log_entry)
        print(f"Sent log: {log_entry}")
    except Exception as e:
        print(f"Error sending log: {e}")

# Read logs line by line
with open(log_file, "r") as file:
    for line in file:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "message": line.strip()
        }
        send_to_elasticsearch(log_entry)
        time.sleep(0.5)  # Simulate real-time log processing
