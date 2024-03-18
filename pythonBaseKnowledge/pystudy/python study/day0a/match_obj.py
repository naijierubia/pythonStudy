"""
 编写一个函数，传入端口名称，返回这个端口运行情况中所描述
的address地址信息。
"""
import re


def get_address(port):
    '''
    :param port: 端口名称
    :return: 端口对应的address
    '''
    f = open('exc.txt')
    while True:
        data = ""
        for line in f:
            if line == '\n':
                break
            data += line
        # 没有找到目标段落
        if not data:
            return "没有该端口"
        obj = re.match(r'\S+', data)  # 使用正则匹配一段首个单词
        if port == obj.group():
            # pattern=r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
            pattern = r'(\d{1,3}\.){3}\d{1,3}/\d{2}|Unknown'
            obj = re.search(pattern, data)
            if obj:
                return obj.group()


if __name__ == '__main__':
    port = input("端口:")
    print(get_address(port))
