import pandas as pd
import jieba.posseg as posseg
# content = "李明喜欢韩梅梅，他俩早恋了"
with open("./datas/鹿鼎记.txt", encoding="utf-8") as fin:
    content = fin.read()
words = []
for word, flag in posseg.cut(content):
    if flag == "nr":
        words.append(word)
print(pd.Series(words).value_counts()[:20])
