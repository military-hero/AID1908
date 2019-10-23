"""
题目004：输入某年某月某日，判断这一天是这一年的第几天？
"""
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
if month < 0 or month > 12:
    print("月份输入错误")
else:
    month_two = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    list01 = (31, month_two, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    day_month = sum(list01[:month - 1])
    day_month += day
    print(day_month)
