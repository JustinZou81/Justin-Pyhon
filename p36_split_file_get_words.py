import pandas as pd
import re

with open("./Beginner Guide to Python.txt", encoding="utf-8") as fin:
    content = fin.read()
# print(content.split())
# \s拆分各种空格，空白符，换行符。符合有.() -?!  +代表一个或者多个
words = re.split(r"[\s.()—?!]+", content)

print(words)
print(pd.Series(words).value_counts()[:20])  # 切片取前20个
