def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("請輸入西元年份: "))
if is_leap_year(year):
    print(year ,"年是閏年")
else:
    print(year ,"年是平年")
