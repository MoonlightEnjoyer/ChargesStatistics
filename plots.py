import matplotlib.pyplot as plt
import numpy as np



def draw_plot(data):

    def func(pct, allvals):
        absolute = pct / 100. * np.sum([float(i) for i in allvals])
        return f"{pct:.2f}BYN\n({absolute:.2f}%)"

    mss_dict = {}

    with open("mcc_list.txt", 'r') as mss_list_file:
        lines = mss_list_file.readlines()
        for line in lines:
            sl = line.split(':')
            mss_dict[sl[0]] = sl[1]

    labels = []

    for key in data.keys():
        labels.append(mss_dict[key])

    values = data.values()

    patches, texts, autotexts = plt.pie(values, autopct=lambda pct: func(pct, data.values()))

    plt.legend(patches, labels, loc="best")

    plt.axis('equal')

    plt.show() 

    