import time
start = time.time()

content = open("input.txt", 'r').readlines()
output = 0

for line in content:
    #print("=============================")
    parts = line.split(' ')
    index_1 = int(parts[0].split('-')[0])
    index_2 = int(parts[0].split('-')[1])
    target = parts[1][0]
    parts[2] = parts[2][:-1]
    
    #print("Index_1: " + str(index_1))
    #print("Index_2: " + str(index_2))
    #print("Target: " + target)
    #print("String: " + parts[2])
    #print("Char1: " + parts[2][(index_1) - 1])
    #print("Char2: " + parts[2][(index_2) - 1])

    if((parts[2][(index_1) - 1] == target and parts[2][(index_2) - 1] != target) or (parts[2][(index_1) - 1] != target and parts[2][(index_2) - 1] == target)):
        #print("Valid")
        output += 1
    #else:
        #print("Invalid")
    #print("=============================")


print(output)

end = time.time()
print("Time Elapsed: " + str(end - start))