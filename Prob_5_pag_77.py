vocale = ['a', 'o', 'i', 'e', 'u', 'A', 'O', 'U', 'E', 'I']
total = []

print('', file=open('input.txt', 'w'))

f = open('input.txt')
for i in f.read():
    if i in vocale:
        total.append(i)
print(f'Vocalele: {total}')
print(f'Sunt {len(total)} vocale')
