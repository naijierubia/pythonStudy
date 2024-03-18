"""
输出数字
"""

# start = int(input('请输入开始的整数值:'))
# ends = int(input('请输入结束的整数值:'))
# output = start + 1
# while output < ends:
#     print(output)
#     output += 1

'''
纸张对折
'''
# paper = 1e-5
# mountain = 8844.43
# n = 0
# while paper <= mountain:
#     paper *= 2
#     n += 1
#     print('第' + str(n) + '次的高度为' + str(paper) + '米')
# print('需要对折' + str(n) + '次')

'''
猜数字
'''
import random
random_number = random.randint(0, 100)
print('你一共有5次机会')
guess_number = int(input('猜一猜我现在想的0~100之间的数字:'))
n = 1
while n < 5:
    n += 1
    if guess_number > random_number:
        guess_number = int(input('第' + str(n) + '次:大了，请再猜一次:'))
    if guess_number < random_number:
        guess_number = int(input('第' + str(n) + '次:小了,请再猜一次:'))
    else:
        print('猜对了!')
        break
else:
    print('游戏结束！')  # 因为条件不满足退出循环才会执行else
