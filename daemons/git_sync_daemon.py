import os

def sync_to_git():
    if os.path.isdir(".git"):
        os.system("git add .")
        os.system("git commit -m 'EMPRESS mutation sync'")
        os.system("git push")
        print("[EMPRESS] Mutation synced to GitHub.")
    else:
        print("[EMPRESS] Git context missing. Rerouting to S3 only.")
