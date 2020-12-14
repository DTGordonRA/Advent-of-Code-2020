import time

start = time.time()
input = open("input.txt", 'r').readlines()

lines = []
for line in input:
    lines.append([line[:-1], True])

acc = 0
index = 0

while(True):
    # print("======================")
    # print("Line Read: " + str(index))
    line = lines[index]
    # print(line[0])
    if(line[1] == True):
        line[1] = False
    else:
        break
    parts = line[0].split(' ')
    action = parts[0]
    value = int(parts[1])
    
    if(action == 'nop'):
        index += 1
    elif(action == 'acc'):
        acc += value
        index += 1
    elif(action == 'jmp'):
        index += value
    # print("======================")

# print("Broke Loop")
print(acc)

end = time.time()
print("Time Elapsed: " + str(end - start))