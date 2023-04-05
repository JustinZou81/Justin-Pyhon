'''for i in range(1, 6):
    if i == 3:
        print('----不走三层')
        continue
    for j in range(1, 9):
        if i==4 and j==4:
            print('遇到鬼屋404房间')
            break
        print(f'L{i}---{i}0{j}室')'''
# for i in range(10):
#     if i <= 5:
#         print('*'*i)
#     else:
#         print('*'*(10-i))
# for i in range(1, 10):

#     for j in range(1, i+1):
#         print(f'{i}*{j}={i*j} ', end='')
#     print()
# name = input("name:")
# age = input('age:')
# hobbie = input('hobbie:')
# msg = f"""
# ------info of {name}------
# Name    :{name}
# Age     :{age}
# Hobbie  :{hobbie}
# -------end-----------
# """
# print(msg)
# for i in range(1, 6):
#     if i == 3:
#         continue
#     for j in range(1, 10):
#         print(f'L{i}----{i}0{j}房')
# salary = int(input('salary:'))
# if salary > 100000:
#     print('公司是我家')
# elif salary > 50000:
#     print('996像呼吸一样自然')
# elif salary > 30000:
#     print('老板说什么都是对的，有人错了，那一定是我')
# elif salary > 20000:
#     print('老板说什么就是什么')
# elif salary > 10000:
#     print('老板说的有问题，但我不说话')
# import random
# c = random.choice('abcdefghijklmnopqrs')
# print(c)
# a = 'abcdefghijklmnopqrs'
# b = random.sample(a, 3)
# print(b)
import random
import string

count = 0
while count < 3:
    car_nums = []  # 存储供用户选择的号
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)  # 生成车牌的第一个字母
        n2 = "".join(random.sample(string.ascii_uppercase+string.digits, 5))
        c_nums = (f"京{n1}-{n2}")
        car_nums.append(c_nums)  # 把生成的号码添加到列表
        print(c_nums)
    choice = input("输入你喜欢的号：")
    if choice in car_nums:  # 代表选择是合法的
        print(f"恭喜你选择了新的车牌号：{choice}")
        exit("Good luck.")
    else:
        print("不合法的选择。。。")
    count += 1
