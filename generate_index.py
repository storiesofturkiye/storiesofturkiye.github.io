import os
import re
from bs4 import BeautifulSoup

# Define available languages
LANGUAGES = [
    "Albanian", "Arabic", "Azerbaijani", "Belarusian", "Bosnian", "Bulgarian", 
    "Chinese", "Danish", "Dutch", "English", "Farsi", "French", "Georgian", 
    "German", "Hungarian", "Italian", "Kazakh", "Korean", "Kyrgyz", "Macedonian", 
    "Malay", "Montenegrin", "Pashto", "Polish", "Romanian", "Russian", "Serbian", 
    "Spanish", "Swedish", "Turkish", "Turkmen", "Ukrainian", "Urdu", "Uzbek"
]

with open('Stories of Türkiye _ Kids Stories.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

imgs = soup.find_all('img')
book_imgs = [img for img in imgs if '36170d_' in img.get('src', '')]

# Usually in Wix, the DOM order matches roughly the screen order, but let's be careful.
# If there are exactly 53 books, we can assign 1 to 53.
print(f"Total book images found: {len(book_imgs)}")

# Sort the books by their Y, then X coordinates on screen if possible,
# or assume the DOM order is correct. Let's assume DOM order.
for i, book_img in enumerate(book_imgs):
    book_num = i + 1
    
    # The parent of the image is wow-image, parent is a, parent is div (ILs2E9)
    # We want to change the href of the anchor tag.
    parent_a = book_img.parent.parent
    if parent_a.name == 'a':
        parent_a['href'] = f'web/English/{book_num}/index.html'
        parent_a['data-book-num'] = str(book_num)
        parent_a['class'] = parent_a.get('class', []) + ['dynamic-book-link']
    else:
        print(f"Warning: Expected <a> tag, found {parent_a.name} for book {book_num}")

# Now we need to inject the language selector.
# We can place it at the top of the body or over the header.
header = soup.find('header')

selector_html = """
<style>
#language-selector-container {
    position: fixed;
    top: 10px;
    right: 10px;
    z-index: 999999;
    background: white;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    font-family: Arial, sans-serif;
    display: flex;
    align-items: center;
    gap: 10px;
}
#language-select {
    padding: 5px;
    font-size: 16px;
    border-radius: 4px;
    border: 1px solid #ccc;
}
</style>
<div id="language-selector-container">
    <label for="language-select"><b>Select Language:</b></label>
    <select id="language-select">
"""
for lang in LANGUAGES:
    selected = ' selected' if lang == 'English' else ''
    selector_html += f'        <option value="{lang}"{selected}>{lang}</option>\n'

selector_html += """
    </select>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
    var select = document.getElementById('language-select');
    var links = document.querySelectorAll('a.dynamic-book-link');
    
    select.addEventListener('change', function() {
        var lang = this.value;
        links.forEach(function(link) {
            var bookNum = link.getAttribute('data-book-num');
            if (bookNum) {
                link.setAttribute('href', 'web/' + lang + '/' + bookNum + '/index.html');
            }
        });
    });
});
</script>
"""

# Append selector exactly at the beginning of the body
if soup.body:
    selector_tag = BeautifulSoup(selector_html, 'html.parser')
    soup.body.insert(0, selector_tag)
else:
    print("Could not find body tag!")

# Remove Wix-specific tracking and annoying popups if possible
# They might have ad iframes or custom scripts causing issues locally

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Created index.html with language selector.")
