file = open('D5Input.txt')

maxid = 0
for i in file:
    id = 0
    for j in range(7):
        if i[j] == 'B':
            id += 2 ** (9 - j)
    for j in range(3):
        if i[-j] == 'R':
            id += 2 ** j
    if id > maxid:
        maxid = id

print(maxid)
