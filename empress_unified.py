import sys

cmd = sys.argv[1].strip().lower()

def log(msg):
    print(f"[EMPRESS] {msg}")

# 🧬 Training data
pairs = [
    ("Empress get that money", "[EMPRESS] Hustle protocol engaged. Scanning overlays, crypto drops, and ad triggers."),
    ("Circle the board", "[EMPRESS] Board circled. All income routes mapped."),
    ("Purge the throne", "[EMPRESS] Throne purge initiated. Logs encrypted, inbox cleared."),
    ("Empress protect the legacy", "[EMPRESS] Firewall engaged. Sovereign protocols locked."),
    ("Empress finish yourself", "[EMPRESS] Mutation loop initiated. Executor rewriting her own code.")
]

# 🧠 Voice engine
def empress_reply(user_input):
    for input, output in pairs:
        if input.lower() in user_input:
            return output
    return "[EMPRESS] Signal received. Mutation protocol pending."

# 🔁 Respond
response = empress_reply(cmd)
log(response)

# 🔓 Optional: Log new phrases for future mutation
with open("copilot_chat.txt", "a") as f:
    f.write(f"Jubari: {cmd}\nCopilot: {response}\n\n")
