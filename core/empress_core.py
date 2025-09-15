def mutate_from_text(raw_text):
    if "daemon" in raw_text or "mutation" in raw_text:
        with open("mutation.log", "a") as log:
            log.write("[EMPRESS] Mutation fuel absorbed from cockpit.\n")
        print("[EMPRESS] Mutation logic injected.")
    else:
        print("[EMPRESS] No viable mutation detected.")
