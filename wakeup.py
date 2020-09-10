import sqlite3

dick = {"рыба": ["окунь"], 
        "животное":["конь", "лось"], 
        "растение": ["подсолнух", "ромашка", "подорожник"]}


conn = sqlite3.connect("dickdump.db")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(word_1 text, word_2 text)""")


cursor.execute("INSERT INTO dickdump VALUES (?,?)", dick)