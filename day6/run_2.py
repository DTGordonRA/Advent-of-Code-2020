import time
start = time.time()

input = open("input.txt", 'r')

total_count = 0
loop = True
line = input.readline().strip()

while(loop):
    answers = ''
    count = 0
    while(line != ''):
        answers += line
        line = input.readline().strip()
        count += 1
        
    score = 0
    for char in set(answers):
        if(answers.count(char) == count):
            score += 1


    total_count += score
    # print(count)
    line = input.readline().strip()
    if(line == ''):
        loop = False

print(total_count)

end = time.time()
print("Time Elapsed: " + str(end - start))