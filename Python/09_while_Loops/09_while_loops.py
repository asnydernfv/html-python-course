i = 0
while i <=10:
    print(f'This is number {i}')
    i += 1
print('The loop is done!')


i = 0
while i <=10:
    if i != 5:
        print(f'This is number {i}')
    else:
        print(f'i = {i}')
        break
    i += 1
print('The loop is done!')