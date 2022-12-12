'''
CS375 Project 4
Aidan Tokarski

Utilities for extracting text from PDF files
'''

import PyPDF2
import re
import os
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io

def pdfparser(file):

    fp = open(file, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        text =  retstr.getvalue()

    text = text.replace("\n", " ")
    text = text.replace("—", " ")
    text = text.replace(".", " ")
    text = text.replace("’", "'")
    text = re.sub(r'[^a-zA-Z\'\- ]', '', text)
    text = text.lower()

    return text

def get_text(file):
    fileReader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in fileReader.pages:
        text += "\n" + page.extract_text()
    text = text.replace("\n", " ")
    text = text.replace("—", " ")
    text = text.replace(".", " ")
    text = text.replace("’", "'")
    text = re.sub(r'[^a-zA-Z\'\- ]', '', text)
    text = text.lower()
    return text

def get_files(dir):
    return os.listdir(dir)

def write_text_file(file, in_dir, out_dir):
    source_file = "{}\{}".format(in_dir, file)
    filename = file.replace(".pdf", "")
    with open("{}\{}.txt".format(out_dir, filename), 'w') as new_file:
        new_file.write(pdfparser(source_file))

if __name__ == "__main__":
    files = get_files("CS375_documents")
    for file in files:
        write_text_file(file, "CS375_documents", "CS375_extracted")