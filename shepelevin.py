def shepelenie(text):
    replacement = {
        "с": "ф",
        "С": "Ф",
        "з": "ф",
        "З": "Ф",
    }
    shepelevin_text = "".join([replacement.get(char, char) for char in text])
    return shepelevin_text