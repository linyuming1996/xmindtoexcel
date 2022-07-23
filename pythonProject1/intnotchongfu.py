"""提取不重复的整数"""
try:
    num = str(input())
    num = num[::-1]
    temp = ''
    for i in num:
        if i not in temp:
            temp = temp+i
    print(temp)
except:
    pass