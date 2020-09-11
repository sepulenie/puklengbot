import sqlite3

dick = {"рыба": ["окунь"], 
        "животное":["конь", "лось"], 
        "растение": ["подсолнух", "ромашка", "подорожник"]}


conn = sqlite3.connect("dickdump.db")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(word_1 text, word_2 text)""")


for word_1 in dick.keys():
        word_2_string = ','.join(dick[word_1])
        cursor.execute("INSERT INTO dickdump VALUES (?,?)", (word_1, word_2_string))
        conn.commit()


sql = "SELECT * FROM dickdump"
cursor.execute(sql)
for row in cursor.execute(sql):
        print(row)