def determine(dx, dy):
    trees = 0
    x, y = 0, 0
    while y < height:
        if map[y][x] == '#':
            trees += 1
        x = (x + dx) % (width - 1)
        y += dy
    return trees


file = open('D3Input.txt')

map = []
for i in file:
    map += [i]
width = len(map[0])
height = len(map)

t1 = determine(1, 1)
t2 = determine(3, 1)
t3 = determine(5, 1)
t4 = determine(7, 1)
t5 = determine(1, 2)

print(t1, t2, t3, t4, t5, t1*t2*t3*t4*t5)
