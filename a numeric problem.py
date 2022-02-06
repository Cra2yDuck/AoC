def remainders(num, divis):
    rems = [0]
    num1 = num
    while num1 % divis != 0:
        rems += [num1 % divis]
        num1 += num
    return rems


def find_a_number(t1, b1, t2, b2):
    a2 = 0
    while (a2 * t2 + b2 - b1) % t1 != 0:
        a2 += 1
    a1 = (a2 * t2 + b2 - b1) // t1
    return a1, a2


x = 67
y1 = 7
y2 = 59
y3 = 61

rems1 = remainders(x, y1)
rems2 = remainders(x, y2)
t1 = len(rems1)
t2 = len(rems2)
b1 = rems1.index(y1 - 1)
b2 = rems2.index(y2 - 2)
a1, a2 = find_a_number(t1, b1, t2, b2)
alp1 = a1 * t1 + b1
alp2 = a2 * t2 + b2
p = alp1 * x

print(rems1)
print(rems2)
print(t1, b1)
print(t2, b2)
print(a1, a2)
print(alp1, alp1 == alp2)
print(p)
print(p%x, (p+1)%y1, (p+2)%y2)
