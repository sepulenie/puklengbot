import re
message = "Из западного Ануса «сосёте: вы» говно За \"Кока-Колу\" сраную продались вы давно. Подстилки подпиндосные!! - Дадим вам пососать? И знать тогда [вы] будете как анусы лизать..."

message = re.findall(r"[\w]+|[^\s\w]", message)       
print(message)