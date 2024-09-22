# find epub files recusively and get the number of pages of each epub file
import shutil
import glob
from bs4 import BeautifulSoup
import zipfile

book_files = glob.glob('**/*.epub', recursive=True)

def extract_epub(epub_file, output_dir):
    with zipfile.ZipFile(epub_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def characters_to_pages(characters):
    # one page is comprised of 1800 characters with spaces
    return characters / 1800

def get_pages(epub_file):
    # unzip the epub file
    extract_epub(epub_file, 'temp')
    # for each html file, get the number of pages
    html_files = glob.glob('temp/**/*.*html', recursive=True)
    characters = 0
    for html_file in html_files:
        html = open(html_file, 'r', encoding='utf-8').read()
        characters += get_pages_html(html)
    # convert characters to pages
    pages = characters_to_pages(characters)
    # delete the temp folder
    shutil.rmtree("temp")
    return pages

def get_pages_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    # convert to a number of pages
    return len(text)

# for book in book_files:
# unzip the epub file
# get the number of html files
# for each html file, get the number of pages
for epub_file in book_files:
    pages = get_pages(epub_file)
    print(epub_file, int(pages))
