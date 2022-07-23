# """字符串个数统计"""
# """编写一个函数，计算字符串中含有的不同字符的个数，字符在ACSII码范围内（0-127），换行表述结束符，不算在字符里，不在范围内的不作统计，多个相同的字符只计算一次"""
# # data = str(input())
# # temp = ''
# # for i in data:
# #     if i not in temp and 0 < ord(i) < 127:
# #         temp = temp + i
# # print(len(temp))
#
# """字符串最后一个单词的长度"""
# data = str(input())
# list = data.split(' ')
# print(len(list[-1]))
#
# """"""

# class Solution(object):
#     def lengthOfLongestSubstring(self,s):
#         sc = {}
#         ans = 0
#         maxans = 0
#         temp = ''
#         for i in s:
#             if i not in temp:
#                 temp += i
#                 ans += 1
#                 if ans > maxans:
#                     maxans = ans
#             elif i in temp:
#                 temp = temp[temp.index(i) + 1:] + i
#                 ans = len(temp)
#         return maxans

""""""
# class Solution:
#     def solve(self , a):
#         if a[0] != 0 :
#             print(0)
#         elif a[-1] != len(a)+1:
#             print(len(a)+1)
#         for i in range(1,len(a)+2):
#             if a[i]-a[i-1] == 2:
#                 print(i)
# a = input()
# index_1 = a.rfind(' ')
# print(len(a)-index_1-1)
# a = input()
# b = input()
# result = a.upper().count(b.upper())
# print(result)
# while True:
#     try:
#         s = input().strip()
#         l = len(s)
#         temp = ''
#         for i in set(s):
#             n = s.count(i)
#             if n < l:
#                 l = n
#         ns = ''
#         for i in s:
#             if s.count(i) !=l:
#                 ns+=i
#         print(ns)
#     except:
#         break
# while True:
#     try:
#         n = input()
#         ta = []
#         for i in range(int(n)):
#             ta.append(int(input()))
#         uniq = set(ta)
#         for i in sorted(uniq):
#             print(i)
#     except:
#         break
