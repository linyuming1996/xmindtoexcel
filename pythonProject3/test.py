#
# while True:
#     try:
#         n = input()
#         temp = ''
#         for i in range(len(n)):
#             if i == 0:
#                 temp += n[i]
#             elif i > 0:
#                 if temp[-1] == n[i]:
#                     temp = temp[:-1]
#                 else:
#                     temp += n[i]
#         print(len(temp))
#     except:
#         break


# while True:
#     try:
#         n = input()
#         sum = 0
#         for i in n:
#             if i.isdigit():
#                 sum += int(i)
#             else:
#                 pass
#         print(sum)
#     except:
#         break
n =input()
list=[]
list= n.split('-')
print(list)
sum=0
for i in n:
    if i.isdigit():
        sum += int(i)
    elif i=='-':
        num = 0
    else:
        pass
print(sum)






