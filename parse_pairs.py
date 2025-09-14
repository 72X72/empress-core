with open("copilot_chat.txt") as f:
    lines = f.readlines()

pairs = []
for i in range(len(lines)-1):
    if lines[i].startswith("Jubari:") and lines[i+1].startswith("Copilot:"):
        input = lines[i].replace("Jubari:", "").strip()
        output = lines[i+1].replace("Copilot:", "").strip()
        pairs.append((input, output))
