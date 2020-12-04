import time
start = time.time()

passports = open("input.txt", 'r')

required_fields = [
    "ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"
]

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
    
    #print(parts)

    line = passports.readline().strip()
    if(line == ''):
        loop = False

print(passport_count)


end = time.time()
print("Time Elapsed: " + str(end - start))