myMap = open("input.txt", 'r').readlines()
treeCount = [0,0,0,0,0]
xIndex = [0,0,0,0,0]
slope = [1,3,5,7]
lineCount = 0

for line in myMap:
    line = line[:-1]
    loopCount = 0
    print("=======================")
    print(line)
    print(lineCount)
    for index in slope:
        print(xIndex[loopCount])
        location = line[xIndex[loopCount]]
        if(location == '#'):
            print('You hit a tree')
            treeCount[loopCount] += 1
        else:
            print("You are safe")
        xIndex[loopCount] = (xIndex[loopCount] + slope[loopCount]) % (len(line) - 1)
        loopCount += 1
    if(lineCount % 2 == 0):
        location = line[xIndex[4]]
        if(location == '#'):
            print('You hit a tree')
            treeCount[4] += 1
        else:
            print("You are safe")
        xIndex[4] = (xIndex[4] + 1) % (len(line) - 1)
    print("=======================")
    lineCount += 1


print(treeCount)
output = treeCount[0]
for i in range(1, len(treeCount)):
    output *= treeCount[i]
print(output)