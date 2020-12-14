import time

def check_num(number, num_pool):
    for i in range(len(num_pool)):
        for j in range(i+1, len(num_pool)):
            if(num_pool[i] + num_pool[j] == number):
                return True
    return False


start = time.time()
input = open("input.txt", 'r')

num_pool = []
for i in range(25):
    num_pool.append(int(input.readline()))

while(True):
    number = int(input.readline())
    if(not check_num(number, num_pool)):
        print(number)
        break
    
    num_pool.append(number)
    num_pool.pop(0)

end = time.time()
print("Time Elapsed: " + str(end - start))