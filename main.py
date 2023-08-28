import pdf_parser
import plots

data = pdf_parser.parse_payments_pdf()

converted_data = {}

for d in data.keys():
    converted_data[d] = abs(sum([eval(i) for i in data[d]]))

plots.draw_plot(converted_data)