

# with open("./datas/student_like.txt", encoding="utf-8") as fin:
#     for line in fin:
#         line = line[:-1]
#         sname, likes = line.split(" ")
#         like_list = likes.split(",")  # 拆出兴趣列别
#         for like in like_list:  # 遍历列表中的每个兴趣
#             if like not in like_count:
#                 like_count[like] = 0
#             like_count[like] += 1   # 将每个兴趣放到字典中进行计数
# print(like_count)
like_count = {}
with open("./datas/student_like.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        sname, likes = line.split(" ")
        like_list = likes.split(",")
        for like in like_list:
            if like not in like_count:
                like_count[like] = 0
            like_count[like] += 1

print(like_count)
