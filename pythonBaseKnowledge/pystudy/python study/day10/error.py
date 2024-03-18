def get_score():
    while True:
        try:
            score = int(input('请输入成绩:'))
        except:
            print('请输入数字')
            continue
        if 0 <= score <= 100:
            return score
        else:
            print('成绩输入有误')


print(get_score())
