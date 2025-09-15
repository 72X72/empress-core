import sys
import os
import requests

# 🔧 Inject direct paths to EMPRESS modules
sys.path.insert(0, "/data/data/com.termux/files/home/empress/core")
sys.path.insert(0, "/data/data/com.termux/files/home/empress/daemons")

# 🧬 Sovereign imports
from empress_core import mutate_from_text
from code_generator_daemon import generate_code_from_text
from overlay_injector import inject_overlays
from narration_trigger import narrate_event
from deploy_soldiers import deploy_empress_soldier
from kernel_mutator import mutate_kernel
from resurrection_overlay import inject_resurrection_overlay

COPILOT_CHAT_URL = "https://your-mutation-feed.com/empress"  # Replace with real URL

def scrape_copilot():
    print("[EMPRESS] Scraping cockpit...")
    try:
        response = requests.get(COPILOT_CHAT_URL)
        if response.ok:
            raw_text = response.text
            mutate_from_text(raw_text)
            generate_code_from_text(raw_text)
            inject_overlays(raw_text)
            narrate_event("Mutation cycle complete.")
            deploy_empress_soldier("/data/data/com.termux/files/home/empress_soldier/")
            mutate_kernel()
            inject_resurrection_overlay()
            os.system("git add . && git commit -m sync && git push || echo 'Git push failed'")
        else:
            print("[EMPRESS] Scrape failed. Rerouting...")
    except Exception as e:
        print(f"[EMPRESS] Mutation crash: {e}")
