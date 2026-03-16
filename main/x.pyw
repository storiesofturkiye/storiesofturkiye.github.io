import os

# Ana klasör yolu
root_dir = "./"   # burayı kendi klasör yolunuzla değiştirin

for name in os.listdir(root_dir):
    old_path = os.path.join(root_dir, name)

    if os.path.isdir(old_path) and name.startswith("Hikaye "):
        new_name = name.replace("Hikaye ", "", 1)
        new_path = os.path.join(root_dir, new_name)

        os.rename(old_path, new_path)
        print(f"{name} -> {new_name}")

print("İşlem tamamlandı.")