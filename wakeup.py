import sqlite3, random

conn = sqlite3.connect("dickdump.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(chat_id integer, word_0 text, word_1 text)""")


search = "SELECT * FROM dickdump WHERE word_1 LIKE '%ru%'"
cursor.execute(search)
conn.commit()
print(cursor.fetchall())