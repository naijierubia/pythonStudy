import random

numbers_q = int(input('请输入需要练习的题目数量：'))
mark = 0
for item in range(1, numbers_q + 1):
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    sum_value = number_1 + number_2
    answer = int(input('第' + str(item) + '道题：' + str(number_1) + '+' + str(number_2) + '='))
    if answer == sum_value:
        print('回答正确，加10分')
        mark += 10
    else:
        print('回答错误，扣5分，正确答案是：' + str(sum_value))
        mark -= 5
print('你的总分为：' + str(mark))
