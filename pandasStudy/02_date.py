import pandas as pd


dates = pd.Series(
    ["2011", "2011-2", "2011-03-01", "2011-04-01 11:11:11", "2011/5/1", "01 Jun 2011"]
)
dates = pd.to_datetime(dates, format="mixed")
print(dates)

""" Series.dt 提供了非常多种日期字段供访问 """
print(dates.dt.year)
print(dates.dt.month)
print(dates.dt.day)
print(dates.dt.hour)
print(dates.dt.minute)
print(dates.dt.second)
print(dates.dt.weekday)
print(dates.dt.quarter)
print(dates.dt.dayofyear)

""" 时间计算 """
delta = pd.to_datetime("now") - dates
print(delta)
# 只有这个属性
print(delta.dt.days)

""" 时间生成 """
# 默认单位是D
# 跳转到月末
dates_1 = pd.date_range("2011-01-01", periods=3, freq="M")
print(dates_1)
# 跳转工作日
dates_2 = pd.date_range("2011-01-01", periods=7, freq="B")
print(dates_2)
# 指定起始点和终点生成