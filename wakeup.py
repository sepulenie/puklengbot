import sqlite3

fish, animal, plant = ["рыба", "окунь"], ["животное", "конь", "лось"], ["растение", "подсолнух", "ромашка", "подорожник"]
mushroom_to_add = ['гриб', 'плесень', 'мухомор', 'слизевик', 'подосиновик']
animal_to_replace = ['животное', 'конь','лось','крыса','кот','пес','голубь','динозавр']
error_to_add = ['лох']

conn = sqlite3.connect("dickdump.db")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(word_1 text, word_2 text)""")


def list_to_tuple(list_to_tuple_var):
        key, value = [list_to_tuple_var[0],' , '.join(list_to_tuple_var[1:])]       
        return key, value

list_to_tuple(animal_to_replace)


def tulpe_to_list(string_to_list = str):
        ready_string = string_to_list.replace


        
def add_to_database(list_to_add_var):
        str_to_add = list_to_tuple(list_to_add_var)
        cursor.execute("INSERT INTO dickdump VALUES (?,?)", (str_to_add[0], str_to_add[1]))
        conn.commit()

#add_to_database(fish)
#add_to_database(animal)
#add_to_database(plant)


def replace_row(list_to_replace):
        str_to_replace = list_to_tuple(list_to_replace)
        print(str_to_replace)
        word_1_to_find = str_to_replace[0]
        print(word_1_to_find)
        search = "SELECT * FROM dickdump WHERE word_1=?"
        cursor.execute(search, [(word_1_to_find)])
        search_result = (cursor.fetchone()[0])
        if search_result == word_1_to_find:
                print('совпадение обнаружено')
                print(search_result)
        else:
                print('совпадений не найдено')
                

def mergelists(list_from_dick, list_to_replace):
        for word_2 in list_to_replace[1:]:
                if word_2 not in list_from_dick[1:]:
                        list

replace_row(animal_to_replace)











'''
key_to_find = 'растение'
search_result = "SELECT * FROM dickdump WHERE word_1=?"
cursor.execute(search_result, [(key_to_find)])
row_to_show = (cursor.fetchone())
if row_to_show == []:
        print('тут нет ничего')
else:
        print(row_to_show)



conn = sqlite3.connect("dickdump.db")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(word_1 text, word_2 text)""")


for word_1 in dick.keys():
        word_2_string = ','.join(dick[word_1])
        cursor.execute("INSERT INTO dickdump VALUES (?,?)", (word_1, word_2_string))
        conn.commit()


key_to_find = 'животное'
search_result = "SELECT * FROM dickdump WHERE word_1=?"
cursor.execute(search_result, [(key_to_find)])
row_to_show = (cursor.fetchone())
if row_to_show == []:
        print('тут нет ничего')
else:
        print(row_to_show)



[[grib, grib_list]] = grib_to_add.items()
grib_to_row = ','.join(grib_list)
cursor.execute("INSERT INTO dickdump VALUES (?,?)", (grib, grib_to_row))
conn.commit()

def replace(list_to_replace = []):
        [[animal, animals_list]] = animal_to_replace.items()
        animal_to_row = ','.join(animals_list)
        print(animal, animal_to_row)
        #cursor.execute("INSERT INTO dickdump VALUES (?,?)", (grib, grib_to_row))
        #conn.commit()

        '''