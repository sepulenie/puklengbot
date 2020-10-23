import sqlite3, random

conn = sqlite3.connect("dickdump.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(chat_id integer, word_0 text, word_1 text)""")


search = "DELETE FROM dickdump WHERE word_1 LIKE '%s=19%'"
cursor.execute(search)
conn.commit()
print(cursor.fetchall())
