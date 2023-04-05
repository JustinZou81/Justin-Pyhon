def read_file():
    result = []
    with open("./student_grade_input.txt", "r") as fin:
        for line in fin:
            line = line[:-1]  # 读取最后一列
            result.append(line)
    return result


# 读文件
datas = read_file()
print(datas)
# 排序数据
# datas = sorted_grades(datas)

# """读取成绩文件排序"""
# import os


# def read_file():
#     result = []
#     with open("./student_grade_input.txt", "r") as fin:
#         for line in fin:
#             line = line[:-1]
#             result.append(line.split(","))
#     return result


# def sort_grades(datas):
#     return sorted(datas,
#                   key=lambda x: int(x[2]),
#                   reverse=True)


# def write_file(datas):
#     print("当前路径", os.getcwd())
#     with open("./student_grade_output.txt", "w") as fout:
#         for data in datas:
#             fout.write(",".join(data)+"\n")


# # 读取文件
# datas = read_file()
# # 排序数据
# datas = sort_grades(datas)

# # 写出文件
# write_file(datas)


# """学生排序"""

# students = [
#     {"son": 101, "sname": "小张", "sgrade": 88},
#     {"son": 102, "sname": "小王", "sgrade": 99},
#     {"son": 103, "sname": "小李", "sgrade": 77},
#     {"son": 104, "sname": "小赵", "sgrade": 68},
# ]

# students_sort = sorted(students,
#                        key=lambda x: x["sgrade"],
#                        reverse=True)
# print(students)
# print(students_sort)

# lista = [20, 40, 30, 50, 10]
# # lista.sort()
# listb = sorted(lista, reverse=True)
# print(f"lista is {lista}")
# print(f"listb is {listb}")

# def get_unique_list(lista):
#     result = []
#     for item in lista:
#         if item not in result:
#             result.append(item)
#     return result


# lista = [10, 20, 30, 10, 20]
# print(f"source list {lista},unique list:", get_unique_list(lista))

# print(f"source list {lista},unique list:", list(set(lista)))
# import math
# print("------阶乘运算-----")


# def get_jiecheng(number):
#     result = 1
#     while number > 0:
#         result *= number
#         number -= 1
#     return result


# print("jiecheng 6=", get_jiecheng(6))
# print("jiecheng 3=", get_jiecheng(3))
# print("jiecheng 100=", get_jiecheng(100))

# number1 = 1.5
# number2 = 3.6

# sum = number1+number2
# print(f"{number1}+{number2}={sum}")

# print("------计算圆的面积------")


# def compute_area_of_cycle(r):
#     return round(math.pi*r*r, 2)


# print("area of 2 is:", compute_area_of_cycle(2))
# print("area of 3.14 is:", compute_area_of_cycle(3.14))
# print("area of 6 is:", compute_area_of_cycle(6))

# print("------打印区间内的素数------")


# def is_prime(number):
#     if number in (1, 2):
#         return True
#     for idx in range(2, number):
#         if number % idx == 0:
#             return False
#     return True


# def print_primes(begin, end):
#     """
#     :para:
#     :return:
#     """
#     for number in range(begin, end+1):
#         if is_prime(number):
#             print(f"{number} is a prime")


# begin = 11
# end = 25
# print_primes(begin, end)

# print("------求前N个数字的平方和------")


# def sum_of_square(n):
#     result = 0
#     for number in range(1, n+1):
#         result += number*number
#     return result


# print("sum of square 3:", sum_of_square(3))
# print("sum of square 5:", sum_of_square(5))

# print("----list 数字加和-----")


# def sum_of_list(param_list):
#     total = 0
#     for item in param_list:
#         total += item
#     return total


# list1 = [1, 2, 3, 4]
# list2 = [17, 5, 3, 5]

# print(f"sum of {list1}", sum_of_list(list1))
# print(f"sum of {list1}", sum_of_list(list2))
