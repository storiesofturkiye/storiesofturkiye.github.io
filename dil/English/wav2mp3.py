import os
from pydub import AudioSegment

input_folder = "./"  # değiştir

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(".wav"):
            wav_path = os.path.join(root, file)
            mp3_path = os.path.splitext(wav_path)[0] + ".mp3"

            try:
                audio = AudioSegment.from_wav(wav_path)
                audio.export(mp3_path, format="mp3")
                print(f"Dönüştürüldü: {mp3_path}")
            except Exception as e:
                print(f"Hata: {wav_path} | {e}")