with open("mss_table.txt", 'r') as src:
    with open('mss_list.txt', 'w') as dst:
        lines = src.readlines()
        for i in range(0, len(lines), 2):
            dst.write(f"{lines[i].strip().replace('MCC ', '')}:{lines[i + 1]}")