import os
import glob
import html

# Base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_DIR = os.path.join(BASE_DIR, 'main')
DIL_DIR = os.path.join(BASE_DIR, 'dil')
WEB_DIR = os.path.join(BASE_DIR, 'web')

# Ensure web directory exists
os.makedirs(WEB_DIR, exist_ok=True)
os.makedirs(os.path.join(WEB_DIR, 'assets'), exist_ok=True)

# HTML Template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Story Book - {language}</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../assets/style.css">
</head>
<body>

    <button id="mute-btn" class="audio-control">🔊 Sesi Kapat</button>

    <div class="book-container">
        <div id="book">
            {pages_html}
        </div>
    </div>

    <script src="https://unpkg.com/page-flip@2.0.7/dist/js/page-flip.browser.js"></script>
    <script src="../../assets/main.js"></script>
</body>
</html>
"""

def clean_text(text):
    lines = text.split('\\n')
    cleaned_lines = []
    for line in lines:
        lower_line = line.lower()
        if any(x in lower_line for x in ["here is the translation", "translated text", "translation:", "important instructions:", "respond only with"]):
            continue
        if not cleaned_lines and not line.strip():
            continue
        cleaned_lines.append(line)
    return '\\n'.join(cleaned_lines).strip()

def generate_book(language, book_id):
    book_dil_dir = os.path.join(DIL_DIR, language, book_id)
    book_main_dir = os.path.join(MAIN_DIR, book_id)
    book_web_dir = os.path.join(WEB_DIR, language, book_id)
    
    if not os.path.exists(book_dil_dir):
        return
        
    os.makedirs(book_web_dir, exist_ok=True)

    pages_html = ""
    
    for page_num in range(1, 23):
        side_class = "--left" if page_num % 2 == 0 else "--right"
        
        img_name = f"page_{page_num}.jpg"
        txt_name = f"page_{page_num}.txt"
        mp3_name = f"page_{page_num}.mp3"
        
        img_path = os.path.join(book_main_dir, img_name)
        txt_path = os.path.join(book_dil_dir, txt_name)
        mp3_path = os.path.join(book_dil_dir, mp3_name)
        
        rel_img_path = f"../../../main/{book_id}/{img_name}"
        rel_mp3_path = f"../../../dil/{language}/{book_id}/{mp3_name}"
        
        has_img = os.path.exists(img_path)
        has_txt = os.path.exists(txt_path)
        has_mp3 = os.path.exists(mp3_path)
        
        if not has_img and not has_txt:
            continue
            
        page_content = ""
        audio_html = ""

        if has_mp3:
            audio_html = f'<audio class="page-audio" src="{rel_mp3_path}" preload="auto"></audio>'
        
        if has_txt:
            with open(txt_path, 'r', encoding='utf-8') as f:
                content = clean_text(f.read())
                safe_content = html.escape(content).strip()
            page_content = f'<div class="page-text">{safe_content}</div>'
        elif has_img:
            page_content = f'<img class="page-image" src="{rel_img_path}" alt="Page {page_num}">'
             
        pages_html += f"""
            <div class="page {side_class}">
                {audio_html}
                <div class="page-content-wrapper">
                    {page_content}
                </div>
                <div class="page-number">{page_num}</div>
            </div>
        """

    output_html = HTML_TEMPLATE.format(
        language=language,
        lang_code=language.lower()[:2], 
        pages_html=pages_html
    )
    
    output_path = os.path.join(book_web_dir, "index.html")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_html)
    
    print(f"Generated {language} - Book {book_id}")

def main():
    if not os.path.exists(DIL_DIR):
        return
    languages = [d for d in os.listdir(DIL_DIR) if os.path.isdir(os.path.join(DIL_DIR, d))]
    for lang in languages:
        lang_dir = os.path.join(DIL_DIR, lang)
        books = [d for d in os.listdir(lang_dir) if os.path.isdir(os.path.join(lang_dir, d))]
        for book in books:
            generate_book(lang, book)

if __name__ == "__main__":
    main()