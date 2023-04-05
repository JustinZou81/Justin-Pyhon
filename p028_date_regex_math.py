import re


def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}", date) is not None  # 简单匹配 {4}代表4个数字


date1 = "2021-05-20"
date2 = "202-05-21"
date3 = "2021/5-20"
date4 = "20210520"
print(date1, date_is_right(date1))
print(date2, date_is_right(date2))
print(date3, date_is_right(date3))
print(date4, date_is_right(date4))
