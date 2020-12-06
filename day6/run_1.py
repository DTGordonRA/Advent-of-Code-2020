import time
start = time.time()

input = open("input.txt", 'r')

total_count = 0
loop = True
line = input.readline().strip()

while(loop):
    answers = ''
    while(line != ''):
        answers += line
        line = input.readline().strip()
        
    answers = set(answers)
    count = len(answers)
    total_count += count
    print(count)
    line = input.readline().strip()
    if(line == ''):
        loop = False

print(total_count)

end = time.time()
print("Time Elapsed: " + str(end - start))