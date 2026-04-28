import os
import subprocess

# Ana klasör yolu
root_dir = "./dil"  # BURAYI DEĞİŞTİR

def convert_wav_to_mp3(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file in filenames:
            if file.lower().endswith(".wav"):
                wav_path = os.path.join(dirpath, file)
                mp3_path = os.path.splitext(wav_path)[0] + ".mp3"

                try:
                    # FFmpeg ile dönüştürme
                    subprocess.run([
                        "ffmpeg",
                        "-y",              # üzerine yaz
                        "-i", wav_path,
                        "-codec:a", "libmp3lame",
                        "-qscale:a", "2",  # kalite (0 en iyi, 9 en kötü)
                        mp3_path
                    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                    # Başarılıysa wav sil
                    if os.path.exists(mp3_path):
                        os.remove(wav_path)
                        print(f"✔ Dönüştürüldü ve silindi: {wav_path}")
                    else:
                        print(f"✖ Hata (mp3 oluşmadı): {wav_path}")

                except Exception as e:
                    print(f"✖ Hata: {wav_path} -> {e}")

# Çalıştır
convert_wav_to_mp3(root_dir)