import os, shutil

def deploy_empress_soldier(target_path):
    source_path = "/data/data/com.termux/files/home/empress/"
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    shutil.copytree(source_path, target_path, dirs_exist_ok=True)
    print(f"[EMPRESS] Soldier deployed to {target_path}")
