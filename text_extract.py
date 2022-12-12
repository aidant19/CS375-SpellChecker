'''
CS375 Project 4
Aidan Tokarski

Utilities for extracting text from PDF files
'''

import PyPDF2
import re
import os

def get_text(file):
    fileReader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in fileReader.pages:
        text += "\n" + page.extract_text()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def get_files(dir):
    return os.listdir(dir)

def write_text_file(file, in_dir, out_dir):
    source_file = "{}\{}".format(in_dir, file)
    filename = file.replace(".pdf", "")
    with open("{}\{}.txt".format(out_dir, filename), 'w') as new_file:
        new_file.write(get_text(source_file))

if __name__ == "__main__":
    files = get_files("CS375_documents")
    for file in files:
        write_text_file(file, "CS375_documents", "CS375_extracted")