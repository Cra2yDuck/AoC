def sorting(inputs):
    evod = [[], []]
    exit1, exit2 = 0, 0
    for i in inputs:
        if i+minNum == 2020 and i != minNum:
            exit1, exit2 = i, minNum
            break
        elif i+minNum < 2020:
            evod[i % 2] += [i]
    return evod, exit1, exit2

def finding(evod):
    for i in evod:
        for j in i[:(len(i)+1)//2]:
            k = 2020-j
            point = len(i)-1
            while i[point] > k:
                point -= 1
            if i[point] == k:
                return j, i[point]


file = open('D1Input.txt')
inputs = []
for i in file:
    inputs += [int(i)]
inputs.sort()
minNum = inputs[0]

evod, exit1, exit2 = sorting(inputs)
if exit1 + exit2 == 2020:
    print(exit1, exit2, exit1*exit2)
else:
    exit1, exit2 = finding(evod)
    print(exit1, exit2, exit1*exit2)



