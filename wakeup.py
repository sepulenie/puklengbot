import csv
dick = {'олень': ['пошел', 'побежал'], 'пошел': 'на', 'хуй': 'блядина', 'такая': 'эдакая'}

with open('dickdump.csv', 'w') as f:
    writer = csv.DictWriter(
        f, fieldnames=list(dick[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in dick:
        writer.writerow(d)