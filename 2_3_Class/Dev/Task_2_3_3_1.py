import random

with open('names.txt', 'w') as file:
    for s in range(100):
        r = str(random.randint(1, 100)) + ' '
        file.write(r+'\n')

with open('names.txt', 'r') as file:
    data = file.read()

list_str = list(data.splitlines())
count = 0
for el in list_str:
    if int(el) % 3 == 0:
        count +=1
print(count)