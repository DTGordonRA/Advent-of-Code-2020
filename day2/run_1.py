import time
start = time.time()

content = open("input.txt", 'r').readlines()
output = 0

for line in content:
    #print(line)
    parts = line.split(' ')
    min_val = int(parts[0].split('-')[0])
    max_val = int(parts[0].split('-')[1])
    target = parts[1][0]
    count = 0
    #print("Min: " + str(min_val))
    #print("Max: " + str(max_val))
    #print("Target: " + target)
    #print("String: " + parts[2])
    for char in parts[2]:
        if(target == char):
            count += 1
    #print("Count: " + str(count))

    if (min_val) <= count <= (max_val):
        #print("Valid")
        output += 1
    #else:
        #print("Invalid")

print(output)

end = time.time()
print("Time Elapsed: " + str(end - start))