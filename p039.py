a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
print("before:")
for i in range(0, len(a)-1):
    print(a[i], end="")
print()
number = int(input("Please inpute the number you want to insert:"))

# 核心代码
local = 0
for i in range(len(a)-2, -1, -1):
    if number > a[i]:
        local = i+1
        break
