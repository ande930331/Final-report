# PYTHON 期中報告
## 11124114黃安德,  11124111王志節
# 題目三:python123题目——判断闰年
# 輸入
*西元年份*
# 輸出
*閏年或平年*
```
def is_leap_year(year):
    if (year % 4 == 0 & year % 100 != 0) | (year % 400 == 0):
        return True
    else:
        return False
```
### 公元年份為4的倍數但非100的倍數公元年份為400的倍數回傳```True``` 否則回傳```False```
```
year = int(input("請輸入西元年份: "))
if is_leap_year(year):
    print(year ,"年是閏年")
else:
    print(year ,"年是平年")
```
