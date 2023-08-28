from PyPDF2 import PdfReader
import re

def parse_payments_pdf():

    reader = PdfReader('data.pdf')
    
    page = reader.pages[0]
    
    text = page.extract_text()

    with open("text_pdf.txt", 'w') as file:
        file.write(text)

    pattern = "/[0-9]{4} -[0-9]+\.[0-9]+"

    x = re.findall(pattern, text)

    splitted_matches = []

    for match in x:
        print(match[1:])
        splitted_matches.append(match[1:].split(' '))

    payments_dict = {}

    for match in splitted_matches:
        if not match[0] in payments_dict.keys():
            payments_dict[match[0]] = []
        payments_dict[match[0]].append(match[1])

    for key in payments_dict.keys():
        print(f'{key} : {payments_dict[key]}')

    return payments_dict
