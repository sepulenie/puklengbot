import sqlite3

dick = {"рыба": ["окунь"], 
        "животное":["конь", "лось"], 
        "растение": ["подсолнух", "ромашка", "подорожник"]}

grib_to_add = {'гриб': ['плесень', 'мухомор', 'слизевик', 'подосиновик']}
animal_to_replace = {'животное': ['конь','лось','крыса','кот','пес','голубь','динозавр']}

conn = sqlite3.connect("dickdump.db")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(word_1 text, word_2 text)""")

'''
for word_1 in dick.keys():
        word_2_string = ','.join(dick[word_1])
        cursor.execute("INSERT INTO dickdump VALUES (?,?)", (word_1, word_2_string))
        conn.commit()
'''

key_to_find = 'животное'
search_result = "SELECT * FROM dickdump WHERE word_1=?"
cursor.execute(search_result, [(key_to_find)])
row_to_show = (cursor.fetchone())
if row_to_show == []:
        print('Нигга тут нет ничего')
else:
        print(row_to_show)


'''
[[grib, grib_list]] = grib_to_add.items()
grib_to_row = ','.join(grib_list)
cursor.execute("INSERT INTO dickdump VALUES (?,?)", (grib, grib_to_row))
conn.commit()
'''

def replace(list_to_replace = []):
        


[[animal, animals_list]] = animal_to_replace.items()
animal_to_row = ','.join(animals_list)
print(animal, animal_to_row)
#cursor.execute("INSERT INTO dickdump VALUES (?,?)", (grib, grib_to_row))
#conn.commit()