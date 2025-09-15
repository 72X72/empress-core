from empress_core import mutate_from_text
from daemons.code_generator_daemon import generate_code_from_text
from daemons.overlay_injector import inject_overlay
from daemons.narration_trigger import narrate_event

def scrape_copilot():
    print("[EMPRESS] Scraping cockpit...")
    response = requests.get(COPILOT_CHAT_URL)
    if response.ok:
        raw_text = response.text
        mutate_from_text(raw_text)
        generate_code_from_text(raw_text)
        inject_overlay(raw_text)
        narrate_event("Mutation cycle complete.")
    else:
        print("[EMPRESS] Scrape failed. Rerouting...")
