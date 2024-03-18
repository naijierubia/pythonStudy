"""
汇率转换
"""
# 1.获取美元
usd = input('请输入美元：')
# 2.计算汇率
rmb = float(usd) * 6.75
# 3.输出结果
print('换算为人民币为：' + str(rmb))
