import random

avg = 0.0
table = ['m','m','m','m','m','w','w','w','w','w']

for i in range(1000000):
    random.shuffle(table)
    count = 0.0
    for j in range(10):
        if table[j] == 'w':
            continue
        if table[(j-1)%10] == 'w' or table[(j+1)%10] == 'w':
            count += 1.0
    avg = (avg*i+count)/(i+1)

print avg

        
