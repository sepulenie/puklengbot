import re
from string import punctuation
from traceback import print_tb
punc = set(punctuation)
message = "Из. западного Ануса «сосёте : вы» говно За \"Кока-Колу\" (That's it - isn't it?), ((сраную... продались вы давно ?"
words_in_message = re.findall(r"[\w]+|[^\s\w]", message)
print(words_in_message)
message = ' '.join(words_in_message)
message = re.sub(r"\s(?=[ , . ! ? : ; — ])", "", message)
message = re.sub(r"(?<=[« \( \] \{ ])\s|\s(?=[»\) \] \} ])", "", message)
message = re.sub(r"(?<=\s\")\s(?=[\w\W]+[\"])", "", message)
message = re.sub(r"(?<=[a-zA-Z])\s(?=['`])|((?<=['`])\s(?=[a-zA-Z]))", "", message)
print(message)




message = ' '.join(words_in_message)
#message = re.sub(r"([\"']+[*\w\W]+[\"])", r" \1 ", message)
