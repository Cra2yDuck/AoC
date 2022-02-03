file = open('D2Input.txt')

inps = [[0, 0, '', ''] for i in range(1000)]

for i in range(1000):
    line = file.readline()
    a, line = line.split('-')
    b, line = line.split(' ', 1)
    c, password = line.split(': ')
    inps[i] = [int(a), int(b), c, password]

s = 0
for i in inps:
    if (i[3][i[0]-1] == i[2]) ^ (i[3][i[1]-1] == i[2]):
        s+=1

print(s)