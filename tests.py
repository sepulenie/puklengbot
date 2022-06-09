import re
message = "Из западного Ануса «сосёте: вы» говно За \"Кока-Колу\" сраную продались вы давно. Подстилки подпиндосные!! - Дадим вам пососать? И знать тогда [вы] будете как анусы лизать..."

message = re.sub(r"http\S+", " ", message)
message = re.sub(r"\S*@\S*\s?", " ", message)
message = re.sub(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", " ", message)
message = re.sub(r'([!@?[]с#%\^&\*\(\):;"\',\./\\]+)', r' \1 ', message)
message = re.sub(r"\n", " ", message)
words_in_message = message.split()        
print(words_in_message)