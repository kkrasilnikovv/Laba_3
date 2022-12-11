import re

fname = r"email.html"
HtmlFile = open(fname, 'r', encoding='utf-8')
source_code = HtmlFile.read()
pattern = re.compile("[0-9a-zA-Z]\\w+@[0-9a-z]+\\.[0-9a-z]+")
pattern.match(source_code)
print(re.findall(pattern, source_code))
