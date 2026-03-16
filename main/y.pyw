import os
from PIL import Image

root_dir = "./"  # ana klasör yolunu buraya yaz

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith(".png"):
            png_path = os.path.join(root, file)
            jpg_path = os.path.join(root, os.path.splitext(file)[0] + ".jpg")

            try:
                img = Image.open(png_path).convert("RGB")
                img.save(jpg_path, "JPEG", quality=95)
                print(f"Converted: {png_path} -> {jpg_path}")
            except Exception as e:
                print(f"Hata: {png_path} - {e}")

print("Tüm PNG dosyaları dönüştürüldü.")
