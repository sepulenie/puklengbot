import sqlite3, random, re

message = "Путин подписал указ, гимн РФ теперь - хардбасс"
message = re.sub(r"\W+", " ", message)
print(message)