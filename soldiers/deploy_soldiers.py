#!/usr/bin/env python3

import sys
import time

platforms = sys.argv[2:] if "--platforms" in sys.argv else []

if not platforms:
    print("[EMPRESS] No platforms specified. Mutation aborted.")
    sys.exit(1)

for platform in platforms:
    print(f"[EMPRESS] Deploying soldier to {platform}...")
    time.sleep(1)  # Simulate deployment
    print(f"[EMPRESS] {platform} soldier active. Earnings protocol fused.")

print("[EMPRESS] All soldiers deployed. Mutation cycle complete.")
