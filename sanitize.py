import regex as re
import string
printable = set(string.printable)

def sanitize(text):
    text = re.sub('<[^<]+?>', '', text)
    text = ''.join(filter(lambda x: x in printable, text))
    text = text.replace(",", "").replace("[", "").replace("]", "").replace("\n", "").replace("\t", "").replace("\\", "")
    return text
