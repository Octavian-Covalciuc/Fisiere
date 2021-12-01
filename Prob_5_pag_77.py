vocale = ['a', 'o', 'i', 'e', 'u', 'A', 'O', 'U', 'E', 'I']
total = []

 with open('input.txt', 'w') as f:
     f.write('')

f = open('input.txt')
for i in f.read():
    if i in vocale:
        total.append(i)
print(f'Vocalele: {total}')
print(f'Sunt {len(total)} vocale')
