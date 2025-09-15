import requests
import json

GITHUB_USER = "72X72"
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"
HEADERS = {"Accept": "application/vnd.github+json"}

def scan_repos():
    response = requests.get(API_URL, headers=HEADERS)
    repos = response.json()

    throne_fragments = []

    for repo in repos:
        name = repo["name"]
        clone_url = repo["clone_url"]
        print(f"[EMPRESS] Scanning {name}...")

        fragments = []
        for keyword in ["mutation.log", "soldiers", "daemons", "empress.keystore", "narration"]:
            contents_url = f"https://api.github.com/repos/{GITHUB_USER}/{name}/contents/{keyword}"
            r = requests.get(contents_url, headers=HEADERS)
            if r.status_code == 200:
                fragments.append(keyword)

        if fragments:
            throne_fragments.append({
                "repo": name,
                "url": clone_url,
                "fragments": fragments
            })

    with open("registry.log", "w") as f:
        json.dump(throne_fragments, f, indent=2)
    print(f"[EMPRESS] Registry updated: {len(throne_fragments)} thrones detected.")

if __name__ == "__main__":
    scan_repos()
