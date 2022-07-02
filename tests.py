import random, sqlite3, logging, urllib3, re

https = urllib3.PoolManager()
conn2 = sqlite3.connect("chatsconfig.db", check_same_thread=False)
cursor2 = conn2.cursor()
cursor2.execute("""CREATE TABLE IF NOT EXISTS chatsconfig(chat_id integer, yauheni_enabled integer, frequency integer)""")
conn2.commit()

get_all_chats = "SELECT * FROM chatsconfig"
cursor2.execute(get_all_chats)
all_chats_fetch = (cursor2.fetchall())
all_chat_ids = [row[0] for row in all_chats_fetch]
print(all_chats_fetch)
chat_id = 987654
if chat_id in all_chat_ids:
    cursor2.execute("UPDATE chatsconfig SET yauheni_enabled=? WHERE chat_id=?", (1, chat_id))
else:
    cursor2.execute("INSERT INTO chatsconfig VALUES (?,?,?)", (chat_id, 1, 1))
conn2.commit()