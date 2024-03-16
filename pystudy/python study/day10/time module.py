import time


# print(time.localtime())
#
# print(time.time())
# print(time.localtime(1661414587.479342))
# # 年 月 日 时 分 秒 星期 天数 夏令时
#
#
# print(time.mktime(time.localtime()))
# # 时间元组变为时间戳
# struct_time = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())
# print(struct_time)
# # 将时间元组转为字符串
#
# print(time.strptime('2022-08-25  16:12:13', '%Y-%m-%d  %H:%M:%S' ))
# # 字符串转为时间元组

def transform_time(year, month, day):
    tuple_time = time.strptime("%d%d%d" % (year, month, day), "%Y%m%d")
    tuple_week = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日')
    return tuple_week[tuple_time[6]]


print(transform_time(2020, 9, 30))


def live_time(year, month, day):
    tuple_now_time = time.localtime()
    tuple_both_time = time.strptime("%d%d%d" % (year, month, day), "%Y%m%d")
    total_day = 0
    total_day += judge_leap_year(year) - tuple_both_time[7]
    for item in range(year + 1, tuple_now_time[0]):
        total_day += judge_leap_year(item)
    total_day += tuple_now_time[7]
    return total_day


def judge_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return 366
    else:
        return 365


print(live_time(2002, 9, 22))


def live_day(year, month, day):
    tuple_time = time.strptime("%d%d%d" % (year, month, day), "%Y%m%d")
    time_second = time.time() - time.mktime(tuple_time)
    return int(time_second / 60 / 60 / 24)


print(live_day(2002, 9, 22))