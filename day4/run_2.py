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

test_count = 0

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
        # print('===========================================================================================================================')
        #print(parts)
        #print(parts['byr'])
        #print(parts['iyr'])
        #print(parts['eyr'])
        if((1920 <= int(parts['byr']) <= 2002) and(2010 <= int(parts['iyr']) <= 2020) and (2020 <= int(parts['eyr']) <= 2030)):
            #print("Passed Year Checks")
            #print(parts['hgt'])
            hgt_pass = False
            hgt_parts = [(parts['hgt'][:-2]), parts['hgt'][-2:]]
            if(hgt_parts[0] != ''):
                hgt_parts[0] = int(hgt_parts[0])
                if(hgt_parts[1] == 'cm'):
                    if(150 <= hgt_parts[0] <= 193):
                        hgt_pass = True
                elif (hgt_parts[1] == 'in'):
                    if(59 <= hgt_parts[0] <= 76):
                        hgt_pass = True
            if(hgt_pass):
                #print('Height Passed')
                #print(parts['hcl'])
                hcl_pass = False
                if(parts['hcl'][0] == '#' and len(parts['hcl']) == 7):
                    hcl_pass = True
                    for char in parts['hcl'][1:]:
                        try:
                            hcl_codes[char]
                        except:
                            hcl_pass = False
                if(hcl_pass):
                    #print("Hair Color Passed")
                    #print(parts['ecl'])
                    ecl_pass = True
                    try:
                        ecl_codes[parts['ecl']]
                    except:
                        ecl_pass = False
                    if(ecl_pass):
                        #print('Eye Color Passed')
                        #print(parts['pid'])
                        pid_pass = False
                        if(len(parts['pid']) == 9):
                            pid_pass = True
                            for char in parts['pid'][1:]:
                                try:
                                    pid_codes[char]
                                except:
                                    pid_pass = False
                        if(pid_pass):
                            # print('PID Passed')
                            passport_count += 1
                            # print(str(passport_count) + ': ' + str(parts))
        # print(parts)
        # print('===========================================================================================================================')

    line = passports.readline().strip()
    if(line == ''):
        loop = False

print("Valid Passports: " + str(passport_count))

end = time.time()
print("Time Elapsed: " + str(end - start))