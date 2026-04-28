from bs4 import BeautifulSoup

# 1. index.html dosyasını oku
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# 2. Tüm "Listen Now" linklerini bul ve sil
for btn in soup.find_all("a", attrs={"aria-label": "Listen Now"}):
    btn.decompose()  # remove() yerine decompose() kullanmak daha temiz

# 3. Yeni dosyaya yaz (veya aynı dosyayı güncelle)
with open("index_updated.html", "w", encoding="utf-8") as file:
    file.write(str(soup))

print("Tüm 'Listen Now' butonları kaldırıldı! index_updated.html oluşturuldu.")