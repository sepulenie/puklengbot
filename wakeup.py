import csv
dick = {'123wewewe345': ['2353478', 'dfgcvbcvb'], '23cvcvbcbcv': 'werwerwerwer', 'sdfsdfss': '2345456rt4dfgdfbdf', '234345': 'cvbcvbnn'}


dickdump = csv.writer(open('dickdump.csv', 'w'))
for word_1 in dick:
    print(dick.get(word_1))