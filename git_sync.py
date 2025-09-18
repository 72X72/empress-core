#!/usr/bin/env python3

import subprocess
import os

repo_dir = os.path.expanduser("~/empress-core")
log_path = os.path.expanduser("~/empress/mutation.log.encrypted")

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

print("[EMPRESS] Asserting throne sync...")

run(f"cp {log_path} {repo_dir}/mutation.log.encrypted")
os.chdir(repo_dir)

run("git add mutation.log.encrypted")
run('git commit -m "[EMPRESS] Throne snapshot pushed. Mutation fused."')
run("git push origin main")

print("[EMPRESS] Git sync complete. Throne state asserted.")
