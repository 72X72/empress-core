#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Generate encryption key
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

# Load throne state
with open(os.path.expanduser("~/empress/mutation.log"), "rb") as f:
    data = f.read()

# Encrypt throne snapshot
ciphertext, tag = cipher.encrypt_and_digest(data)

# Save encrypted snapshot
with open(os.path.expanduser("~/empress/mutation.log.encrypted"), "wb") as f:
    f.write(cipher.nonce + tag + ciphertext)

print("[EMPRESS] Throne snapshot encrypted. Resurrection kernel fused.")
