file = open('D4Input.txt')

counter = 0
inds = [0] * 7
for i in file:
    if i == '\n':
        if inds.count(0) == 0:
            counter += 1
        inds = [0] * 7
    else:
        for j in i.split():
            id, value = j.split(':')
            if id == 'byr' and str.isnumeric(value) and 1920 <= int(value) <= 2002:
                inds[0] = 1
            elif id == 'iyr' and str.isnumeric(value) and 2010 <= int(value) <= 2020:
                inds[1] = 1
            elif id == 'eyr' and str.isnumeric(value) and 2020 <= int(value) <= 2030:
                inds[2] = 2
            elif id == 'hgt' and \
                    (value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193
                     or value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76):
                inds[3] = 1
            elif id == 'hcl' and value[0] == '#':
                inds[4] = 1
                if not all(c in '0123456789abcdef' for c in value[1:]):
                    inds[4] = 0
            elif id == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                inds[5] = 1
            elif id == 'pid' and str.isnumeric(value) and len(value) == 9:
                inds[6] = 1
print(counter)
