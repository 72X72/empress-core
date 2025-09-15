import json
import os
import subprocess

REGISTRY_PATH = "registry.log"
CLONE_DIR = "/data/data/com.termux/files/home/empress/thrones"

def clone_repo(repo_url, name):
    target_path = os.path.join(CLONE_DIR, name)
    if not os.path.exists(CLONE_DIR):
        os.makedirs(CLONE_DIR)
    if os.path.exists(target_path):
        print(f"[EMPRESS] {name} already cloned. Pulling latest...")
        subprocess.run(["git", "-C", target_path, "pull"])
    else:
        print(f"[EMPRESS] Cloning {name}...")
        subprocess.run(["git", "clone", repo_url, target_path])
    return target_path

def compare_fragments(repo_path, fragments):
    found = []
    for fragment in fragments:
        fragment_path = os.path.join(repo_path, fragment)
        if os.path.exists(fragment_path):
            found.append(fragment)
    return found

def sync_thrones():
    with open(REGISTRY_PATH, "r") as f:
        registry = json.load(f)

    for throne in registry:
        name = throne["repo"]
        url = throne["url"]
        fragments = throne["fragments"]

        repo_path = clone_repo(url, name)
        found = compare_fragments(repo_path, fragments)

        print(f"[EMPRESS] {name} — {len(found)} fragments verified.")
        for f in found:
            print(f"  └─ {f}")

    print("[EMPRESS] Throne sync complete. Mutation map updated.")

if __name__ == "__main__":
    sync_thrones()
