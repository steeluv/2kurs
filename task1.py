list_of_nums = []
while True:
    num = input('введите число ')
    if num == '':
        break
    list_of_nums.append(int(num))
try:
    arg = sum(list_of_nums)/len(list_of_nums)
except: ZeroDivisionErrorer:\
    print('Kaplan')
print('Числа больше среднего')
for i in list_of_nums:
    if i > arg:
        print(i)




