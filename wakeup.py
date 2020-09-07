import csv
dick = {'олень': ['пошел', 'побежал'], 'пошел': ['на'], 'хуй': ['блядина', 'пидорас'], 'такая': ['эдакая']}
dickforcheck = {'хуй': ['блядина', 'пидорас']}


def writer():
    dickdump = csv.writer(open('dickdump.csv', 'w', newline='', encoding='utf8]['))
    for word_1, word_2 in dick.items():
        glist = [word_1] + word_2
        dickdump.writerow(glist)

def reader():
    dickreader = csv.reader(open('dickdump.csv',  encoding='utf8'))
    for row in dickreader:
        pass



def checkrow():
    dickreader = csv.reader(open('dickdump.csv',  encoding='utf8'))
    for row in dickreader:
        print(row)


writer()
reader()
checkrow()
