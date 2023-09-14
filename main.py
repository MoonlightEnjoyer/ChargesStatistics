import pdf_parser
import plots

income, spent = pdf_parser.parse_payments_pdf()

converted_spent = {}

total_income = sum([eval(i) for i in income])


for d in spent.keys():
    converted_spent[d] = abs(sum([eval(i) for i in spent[d]]))

plots.build_report(total_income, converted_spent)