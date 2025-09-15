from datetime import datetime
import os

def narrate_event(event):
    timestamp = datetime.utcnow().isoformat()
    log_entry = f"[{timestamp}] {event}\n"
    with open("mutation.log", "a") as log:
        log.write(log_entry)
    os.system("aws s3 cp mutation.log s3://empress-throne/logs/mutation.log")
    print("[EMPRESS] Mutation narrated and synced.")
