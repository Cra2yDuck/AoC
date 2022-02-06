file = open('D4Input.txt')

counter = 0
inds = [0] * 8
pointers = {'byr': 0, 'iyr': 1, 'eyr': 2, 'hgt': 3, 'hcl': 4, 'ecl': 5, 'pid': 6, 'cid': 7}
for i in file:
    if i == '\n':
        if inds.count(0) == 0 or (inds.count(0) == 1 and inds[7] == 0):
            counter += 1
        inds = [0] * 8
    else:
        for j in i.split():
            ind, value = j.split(':')
            inds[pointers[ind]] = 1

print(counter)
