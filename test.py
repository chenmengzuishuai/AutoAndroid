import re

a = "adfadfdaekdfeiasdklfadf"

b = re.findall(r'.*(\w{3,})(\1).*', a)
b = re.search(r'.*(\w{3,})\1.*', a)
print(b)