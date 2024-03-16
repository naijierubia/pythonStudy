import re

s = "Alex:1996, Tom:1998"
pattern = r"(\w+):(\d+)"

# 使用re
l = re.findall(pattern, s)
print(l)

# compile对象
regex = re.compile(pattern)
l = regex.findall(s)
print(l)
l = regex.findall(s, 0, 13)
print(l)

# split切割字符串
l = re.split(r'[^\w]', s)
print(l)

# sub替换
# subn替换,额外返回替换几次
l = re.sub(r':', "--", s )
print(l)
l = re.subn(r':', "--", s )
print(l)

# match匹配开始的字符
# fullmatch完全匹配
# search匹配第一个
# findite返回匹配的可迭代对象
