# import os

# sum_size = 0
# for file in os.listdir("."):
#     if os.path.isfile(file):
#         sum_size = os.path.getsize(file)
# print("all size of dir:", sum_size/1000)

import os
import shutil
# dir = "E:\下载"
# for file in os.listdir(dir):
#     ext = os.path.splitext(file)[1]  # 返回的是元祖，后缀取1
#     ext = ext[1:]
#     if not os.path.isdir(f"{dir}/{ext}"):
#         os.mkdir(f"{dir}/{ext}")
#     print(file, ext)

dir = "E:\下载"
for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")

    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.move(source_path, target_path)