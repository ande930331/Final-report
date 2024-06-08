#PYTHON 期中報告
11124114黃安德,  11124111王志節
# 題目三:python123题目——判断闰年
```
def is_leap_year(year):
    if (year % 4 == 0 & year % 100 != 0) | (year % 400 == 0):
        return True
    else:
        return False
```
公元年份為4的倍數但非100的倍數，為366天閏年/n
公元年份為400的倍數，（1600年及2000年）為閏年
