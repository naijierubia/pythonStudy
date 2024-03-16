"""
自定义生成器
"""
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b 
        a, b = b, a + b
        n += 1


for n in fab(10):
    print(n)


class MyRange:
    def __init__(self, stop=0):
        self.stop = stop

    def __iter__(self):
        number = 0
        while number < self.stop:
            yield number
            number += 1


for item in MyRange(10):
    print(item)
# generator 可以根据算法生成数据，而不用将数据存在列表中，从而节省了内存
