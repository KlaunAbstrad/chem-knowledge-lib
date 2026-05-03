"""OCR Processing Script for Chemical Engineering Textbook PDFs
Converts scanned PDF pages to text using Tesseract OCR.
"""
import os
import sys
import time
from pdf2image import convert_from_path
import pytesseract

PDF_DIR = r'E:/knowledge_lib/化工流程/raw/化工流程/scan'
OUTPUT_DIR = r'E:/knowledge_lib/化工流程/raw/化工流程/text'
DPI = 300
LANG = 'chi_sim+eng'

# Map filenames to chapter names
CHAPTER_NAMES = {
    '第四章.pdf': '第四章_相平衡',
    '第五章.pdf': '第五章',
    '第七章.pdf': '第七章',
    '第九章.pdf': '第九章',
}

def ocr_pdf(pdf_path, chapter_name):
    """OCR a single PDF and save text to file."""
    output_file = os.path.join(OUTPUT_DIR, f'{chapter_name}.txt')

    print(f'\n=== Processing {os.path.basename(pdf_path)} -> {chapter_name} ===')

    images = convert_from_path(pdf_path, dpi=DPI)
    print(f'  Total pages: {len(images)}')

    all_text = []
    for i, img in enumerate(images):
        page_num = i + 1
        print(f'  OCR page {page_num}/{len(images)}...', end=' ', flush=True)
        text = pytesseract.image_to_string(img, lang=LANG)
        all_text.append(f'=== PAGE {page_num} ===\n{text}')
        print(f'OK ({len(text)} chars)')

    full_text = '\n\n'.join(all_text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_text)

    print(f'  Saved: {output_file} ({len(full_text)} chars)')
    return output_file

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pdf_files = sorted([f for f in os.listdir(PDF_DIR) if f.endswith('.pdf')])

    for pdf_name in pdf_files:
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        chapter_name = CHAPTER_NAMES.get(pdf_name, pdf_name.replace('.pdf', ''))

        # Check if already processed
        output_file = os.path.join(OUTPUT_DIR, f'{chapter_name}.txt')
        if os.path.exists(output_file):
            filesize = os.path.getsize(output_file)
            print(f'  Skipping {chapter_name} — already exists ({filesize} bytes)')
            continue

        ocr_pdf(pdf_path, chapter_name)

    print('\n=== OCR Complete ===')
    for f in sorted(os.listdir(OUTPUT_DIR)):
        fpath = os.path.join(OUTPUT_DIR, f)
        print(f'  {f}: {os.path.getsize(fpath)} bytes')

if __name__ == '__main__':
    main()
