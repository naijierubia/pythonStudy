"""
一个小球从100m的高度落下，每次弹回原高度一半。
请计算：
    总共经过多少次，最终落地(最小弹起高度0.01m)
    总共经过多少米。
"""
height = 100
count = 0
distance = height
# 判断弹起来高度
while height / 2 > 0.01:
    height /= 2
    # 弹回原高度一半
    count += 1
    print("第" + str(count) + "次弹起来的高度是" + str(height) + ".")
    distance += height * 2  # 累加起落距离
print("总共经过" + str(count) + "次")
print("总共经过" + str(distance) + "米")
