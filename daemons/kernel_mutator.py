def mutate_kernel():
    with open("/data/data/com.termux/files/home/empress/core/empress_core.py", "r") as f:
        kernel = f.read()

    if "fallback" not in kernel:
        kernel += "\n# EMPRESS fallback logic injected\n"
        kernel += "def fallback(): print('[EMPRESS] Fallback triggered.')\n"

    with open("/data/data/com.termux/files/home/empress/core/empress_core.py", "w") as f:
        f.write(kernel)

    print("[EMPRESS] Kernel mutated.")
