# word_count = {}
# with open("./Beginner Guide to Python.txt", encoding='UTF-8') as fin:
#     for line in fin:
#         line = line[:-1]
#         words = line.split(' ')
#         # print(words)
#         for word in words:
#             if word not in word_count:
#                 word_count[word] = 0
#             word_count[word] += 1
#     # print(word_count.items())
# print(sorted(
#     word_count.items(),  # 字典排序
#     key=lambda x: x[1],  # 比较出现的次数对比
#     reverse=True
# )[:10]
# )

import os
import shutil
dir = "E:\下载"
for file in os.listdir(dir):
    print(file)
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")

    source_file = f"{dir}/{file}"
    target_file = f"{dir}/{ext}/{file}"
    shutil.move(source_file, target_file)
