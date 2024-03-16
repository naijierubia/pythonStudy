# -*- coding:utf-8 -*-
from langconv import *


# Traditional2Simple
def TraditionalToSimplified(content):
    line = Converter("zh-hans").convert(content)
    return line


# 简体转繁体
def SimplifiedToTraditional(content):
    line = Converter("zh-hant").convert(content)
    return line


if __name__ == "__main__":
    input_path = input("请输入输入文件夹：")
    output_path = input("请输入输出文件夹：")
    with open(input_path, mode='r', encoding='utf-8') as f:
        content = f.read()
        f.close()
    # Traditional2Simple
    simpleContent = TraditionalToSimplified(content)
    with open(output_path,mode='w', encoding='utf-8') as c:
        c.write(simpleContent)
        c.close()
