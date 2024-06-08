# PYTHON 期中報告
## 11124114黃安德,  11124111王志節
# 題目三:判断闰年
### 公元年份為4的倍數但非100的倍數或公元年份為400的倍數回傳```True``` 否則回傳```False```
```
def is_leap_year(year):
    if (year % 4 == 0 & year % 100 != 0) | (year % 400 == 0):
        return True
    else:
        return False
```
```
year = int(input("請輸入西元年份: "))
if is_leap_year(year):
    print(year ,"年是閏年")
else:
    print(year ,"年是平年")
```
# 實利:回傳閏年
