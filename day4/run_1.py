import time
start = time.time()

passports = open("input.txt", 'r')

required_fields = [
    "ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"
]

hcl_codes = {'0':1, '1':1, '2':1, '3':1, '4':1, '5':1, '6':1, '7':1, '8':1, '9':1, 'a':1, 'b':1, 'c':1, 'd':1, 'e':1, 'f':1}
ecl_codes = {"amb":1,"blu":1,"brn":1,"gry":1,"grn":1,"hzl":1,"oth":1}
pid_codes = {'0':1, '1':1, '2':1, '3':1, '4':1, '5':1, '6':1, '7':1, '8':1, '9':1}

loop = True
line = passports.readline().strip()

passport_count = 0

while(loop):
    parts = {}
    valid = True

    while(line != ''):
        for part in line.split(' '):
            keyval = part.split(':')
            parts[keyval[0]] = keyval[1]
        line = passports.readline().strip()
        
    for field in required_fields:
        try:
            parts[field]
        except:
            valid = False
            break

    if(valid == True):
        passport_count += 1
    
    print(parts)

    line = passports.readline().strip()
    if(line == ''):
        loop = False

print(passport_count)


end = time.time()
print("Time Elapsed: " + str(end - start))