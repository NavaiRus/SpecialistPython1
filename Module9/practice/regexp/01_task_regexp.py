import re

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
p= r"\b[A-Z]\w{4}\b"
p1= r"\b\w{2}"
p2= r"\b[aeioyu]\w+\b"
p3= r"\b[^ aeioyu]\w+\b"
p4= r"[^ \w ]"
print(re.findall(p, text))
print(re.findall(p1, text))
print(re.findall(p2, text))
print(re.findall(p3, text))
print(re.findall(p4, text))
