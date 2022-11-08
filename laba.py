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
nul = 1
for i in range(0, len(my_list),3):
    print(f'{nul} * {my_list[i]}{[i]}=', end=' ')
    nul += my_list[i]
    print(nul)
sum_list =[0] * 3
for i in my_list:
    if i < 0:
        sum_list[0] += i
    if i % 2 == 0:
        sum_list[1] += i
    if i % 2 != 0:
        sum_list[2] += i
print(f'Sum negative:{sum_list[0]}')
print(f'Sum even:{sum_list[1]}')
print(f'Sum odd:{sum_list[2]}')
print(f'Nul even:{nul}')

nul = 1
start_index = my_list.index(min(my_list))
end_index = my_list.index(min(my_list))
if start_index > end_index:
    start_index, end_index = end_index, start_index
print(f'start_index = {start_index}, end_index = {end_index}')
for i in range(start_index+1, end_index):
    print(f'{my_list[i]}', end=' ')
    nul += my_list[i]
print(f'\n Nul = {nul}')



