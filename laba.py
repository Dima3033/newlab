import random
s = int(input('size ->'))
begin = int(input('begin ->'))
end = int(input('end ->'))
my_list = list()
for i in range(s):
    my_list.append(random.randint(begin, end))
for i in my_list:
    print(f'{my_list.index(i)}{[i]}', end=" ")
print()
result_list_even = list()
result_list_odd = list()
result_list_negative = list()
result_list_positive = list()
for i in my_list:
    if i % 2 == 0:
        result_list_even.append(i)
    if i % 2 != 0:
        result_list_odd.append(i)
    if i < 0:
        result_list_negative.append(i)
    if i > 0:
        result_list_positive.append(i)
print(f'list even : {result_list_even}')
print(f'list odd : {result_list_odd}')
print(f'list negative : {result_list_negative}')
print(f'list positive : {result_list_positive}')
