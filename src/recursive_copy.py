import os
import shutil


def recursive_copy(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest, exist_ok=True)
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)        
        if os.path.isdir(src_path):
            recursive_copy(src_path, dest_path)
        else:
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {dest_path}")