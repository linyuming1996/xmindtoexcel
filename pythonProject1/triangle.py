list1 = [1]
list2 = [1]
n = int(input('请输入输出的行数：'))
for i in range(n):
    for y in range(i+1):
        if y == 0:
            list2[y] = 1
        elif 0 < y < i:
            list2[y] = list1[y]+list1[y-1]
        else:
            list2.append(1)
    for y in list2:
        print(y, end=' ')
    print()
    list1 = list2.copy()


# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1