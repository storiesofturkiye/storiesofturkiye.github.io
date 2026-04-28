from bs4 import BeautifulSoup

with open('Stories of Türkiye _ Kids Stories.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

imgs = soup.find_all('img')
books = [img for img in imgs if '36170d_' in img.get('src', '')]

print(f'Found {len(books)} book images.')
if books:
    book = books[0]
    # Go up a few parents
    parent = book.parent
    for i in range(5):
        if parent:
            print(f'--- Parent {i+1} ---')
            print(f'Tag: {parent.name}, classes: {parent.get("class")}, id: {parent.get("id")}')
            parent = parent.parent

    # Let's extract the full outer HTML of a book container
    # Assuming parent 3 or 4 is the grid item
    item = books[0].parent.parent.parent.parent
    print('\n--- Item HTML ---')
    print(str(item)[:500])
