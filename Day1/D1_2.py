file = open('D1Input.txt')
inputs = []
f = 0
for i in file:
    inputs += [int(i)]

l = len(inputs)
for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if inputs[i]+inputs[j]+inputs[k] == 2020:
                s = inputs[i]*inputs[j]*inputs[k]
                f = 1
                break
        if f == 1:
            break
    if f == 1:
        break

print(s)