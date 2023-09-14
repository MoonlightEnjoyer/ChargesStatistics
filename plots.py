import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader

def build_report(income, data):
    height = 1.5
    c = canvas.Canvas("Figures.pdf")
    c.setTitle("Figures")
    mss_dict = {}
    with open("mcc_list.txt", 'r') as mss_list_file:
        lines = mss_list_file.readlines()
        for line in lines:
            sl = line.split(':')
            mss_dict[sl[0]] = sl[1]

    labels = []

    for key in data.keys():
        labels.append(mss_dict[key])

    draw_plot(c, data.values(), labels, height)
    draw_plot(c, [income, np.sum([float(i) for i in data.values()])], ['income', 'spent'], height + 15)
    c.save()


def draw_plot(c, values, labels, height):

    def func(pct, allvals):
        absolute = pct / 100. * np.sum([float(i) for i in allvals])
        return f"{pct:.2f}%\n({absolute:.2f} BYN)"

    figure, ax1 = plt.subplots()

    patches, texts, autotexts = ax1.pie(values, labeldistance=0.75, autopct=lambda pct: func(pct, values))

    plt.legend(patches, labels, bbox_transform=plt.gcf().transFigure, loc="center right")

    plt.axis('equal')

    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax1.axis('equal') 

    plt.tight_layout()

    #plt.show() 

    dpi = figure.get_dpi()
    figureSize = figure.get_size_inches()    

    image = BytesIO()
    figure.savefig(image, format="png")
    image.seek(0)
    image = ImageReader(image)

    figureSize = figure.get_size_inches()*1

    c.drawImage(image, (10.5-figureSize[0]/2)*cm, height*cm,
                figureSize[0]*cm, figureSize[1]*cm)