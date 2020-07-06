import re

pattern = re.compile('this')

string = 'search inside this string'


a = pattern.search(string)
b = pattern.findall(string)

print(b)