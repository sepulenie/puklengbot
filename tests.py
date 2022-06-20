import re
message = 'Я ебал тебя в жопу \n ебал тебя в рот,  ты тупая скотина, не позорь ты народ.\n\nСкотобаза ебаная блядь'
message = re.sub(r"http\S+", " ", message)
message = re.sub(r"\S*@\S*\s?", " ", message)
message = re.sub(r">"," ", message)
message = re.sub(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", " ", message)
message = re.sub(r"(?<=[\w\s])\n+", ". ", message)
message = re.sub(r"\n", " ", message)
message = re.sub(r"\s-\s", ' — ',message)
print(message)