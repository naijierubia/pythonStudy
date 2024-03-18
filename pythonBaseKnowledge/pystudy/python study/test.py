import re


reg = r"\[(\d{1,2}):(\d{1,2}.\d{1,3})\](.*)"
lrc = "[00:00.000] 作词 : 有里泉美"
print(re.match(reg, lrc)[3])


# 使用正则表达式匹配时间、秒、毫秒和歌词信息
result = re.findall(r'\[(\d{2}:\d{2}.\d{3})\] (.*)', lrc)

# 打印结果
for item in result:
    print("时间:", item[0])
    print("歌词:", item[1])
