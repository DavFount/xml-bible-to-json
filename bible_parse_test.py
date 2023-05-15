import os
import json
import xml.etree.ElementTree as ET

path = './bibles/'
for filename in os.listdir(path):
    if not filename.endswith('.xml'):
        continue
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)
    root = tree.getroot()

    bible = []

    for book in root:
        book_data = {
            "number": book.attrib['bnumber'],
            "name": book.attrib['bname'],
            "chapters": []
        }
        for chapter in book:
            chapter_number = chapter.attrib['cnumber']
            verses = []
            for verse in chapter:
                verses.append(verse.text.strip())

            book_data["chapters"].append(verses)
        bible.append(book_data)

    output_name = filename.replace('.xml', '')
    with open(f"./parsed/{output_name}.json", "w", encoding='utf8') as outfile:
        json.dump(bible, outfile, ensure_ascii=False)
