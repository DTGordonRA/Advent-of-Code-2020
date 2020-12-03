import time
start = time.time()

myMap = open("input.txt", 'r').readlines()
treeCount = 0
xIndex = 0
lineCount = 0

for line in myMap:
    line = line[:-1]
    location = line[xIndex]
    test = line
    test = test[:xIndex] + 'X' + test[xIndex + 1:]
    #print("=======================")
    #print(line)
    #print(test)
    #print(lineCount)
    #print(xIndex)
    #print(location)
    if(location == '#'):
        #print('You hit a tree')
        treeCount += 1
    #else:
        #print("You are safe")
    lineCount += 1
    xIndex = (xIndex + 3) % (len(line) - 1)
    #print("=======================")


print(treeCount)

end = time.time()
print("Time Elapsed: " + str(end - start))