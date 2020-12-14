import time
stack_size = 25

def check_num(number, num_pool, index, stack_size):
    for i in range(index, stack_size + index):
        for j in range(index + 1, stack_size + index):
            if(num_pool[i] + num_pool[j] == number):
                return True
    return False


def check_sum_numbers(target, num_pool):
    set_size = 2
    while(True):
        #print("Set Size: " + str(set_size))
        for i in range(len(num_pool) - set_size):
            numbers = sum_numbers(i, num_pool, set_size)
            #print(numbers)
            if(sum(numbers) == target):
                print("Set Found")
                print(numbers)
                return numbers
        set_size += 1
        if(set_size == len(num_pool)):
            print("No Set Found")
            return False

def sum_numbers(index, num_pool, counters):
    output = [num_pool[index]]
    if(counters > 1):
        output += sum_numbers(index + 1, num_pool, counters - 1)
    return output


start = time.time()
input = open("input.txt", 'r').readlines()

num_pool = []
for line in input:
    num_pool.append(int(line))

counter = 0
target_number = 0
while(True):
    number = num_pool[stack_size + counter]

    if(not check_num(number, num_pool, counter, stack_size)):
        print(number)
        target_number = number
        break
    
    counter += 1

num_pool_copy = (num_pool[:])
num_pool_copy.pop(counter + stack_size)

#Remove values grater than the target number
#Work with indexes so it doesn't have to search the array for each value
to_remove = []
for i in range(len(num_pool_copy)):
    if(num_pool_copy[i] > target_number):
        # Will throw error if removed here so save then remove in next loop
        to_remove.append(i)
counter = 0
for i in to_remove:
    num_pool_copy.pop(i - counter)
    counter += 1

output = check_sum_numbers(target_number, num_pool_copy)
if(output != False):
    for i in range(len(output) - 1):
        for j in range(len(output) - 1):
            if(output[j] > output[j+1]):
                output[j], output[j + 1] = output[j + 1], output[j]
    print(output[0] + output[-1])

end = time.time()
print("Time Elapsed: " + str(end - start))