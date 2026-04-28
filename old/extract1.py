from bs4 import BeautifulSoup
import sys

with open('Stories of Türkiye _ Kids Stories.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

links = soup.find_all('a')
print('=== LINKS ===')
for i, a in enumerate(links):
    href = a.get('href', '')
    if 'com/' in href or '#' in href or not href:
        continue
    print(f'Link: href={href} text={a.text.strip()}')

# Let's find images
imgs = soup.find_all('img')
print('=== IMGS ===')
for i, img in enumerate(imgs):
    src = img.get('src', '')
    if 'wixstatic' not in src:
        print(f'Image: src={src} alt={img.get("alt")}')
