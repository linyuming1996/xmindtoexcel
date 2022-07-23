"""非连续序列"""
xulie = input('xulie:')
print(xulie)
temp = '1'
temp1 = '1'
a = 0
while a < len(xulie):
    if xulie[a].isdigit() and temp == '':
        temp = temp+xulie[a]
    elif xulie[a].isdigit() and temp != '' and xulie[a] >= temp[-1]:
        temp = temp+xulie[a]
        if len(temp) >= len(temp1):
            temp1 = temp
    elif xulie[a].isalnum() and temp != '' and xulie[a] <= temp[-1]:
        temp = ''+xulie[a]
    elif xulie[a].isalpha():
        temp = ''
    a += 1
print(temp1+' len='+str(len(temp1)))