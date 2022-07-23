"""功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（如180的质因子为2 2 3 3 5 ）"""
n = int(input())
for i in range(2,n+1):
    while n % i ==0:
        print(i, end=' ')
        n = n / i
    if n == 1:
        break