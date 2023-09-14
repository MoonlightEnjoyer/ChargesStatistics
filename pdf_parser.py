from PyPDF2 import PdfReader
import re


def parse_payments_pdf():

    reader = PdfReader('data.pdf')
    
    page = reader.pages[0]
    
    text = page.extract_text()

    with open("text_pdf.txt", 'w') as file:
        file.write(text)

    spent_pattern = "/[0-9]{4} -[0-9]+\.[0-9]+"
    income_pattern = "[0-9]{2}:[0-9]{2}:[0-9]+/[\w|\s]+/ [0-9]+\.[0-9]+ BYN"
    income_value_pattern = "[0-9]+\.[0-9]+"

    x_income = re.findall(income_pattern, text)
    x_spent = re.findall(spent_pattern, text)
    

    splitted_spent = []
    splitted_income = []

    for match in x_spent:
        #print(match[1:])
        splitted_spent.append(match[1:].split(' '))

    for match in x_income:
        #print(match[1:])
        splitted_income.append(re.findall(income_value_pattern, match)[0])

    spent_dict = {}

    for match in splitted_spent:
        if not match[0] in spent_dict.keys():
            spent_dict[match[0]] = []
        spent_dict[match[0]].append(match[1])

    for key in spent_dict.keys():
        print(f'{key} : {spent_dict[key]}')

    return splitted_income, spent_dict