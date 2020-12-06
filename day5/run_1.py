import time
start = time.time()

data = open("input.txt", 'r').readlines()

highest_number = 0
highest_str = ''

seating_map = {}


for line in data:
    #print('=====================================================================================')
    #print(line)
    row_str = line[:7]
    col_str = line[7:].strip()
    
    row_num = 0
    col_num = 0

    #print(row_str)
    for i in range(len(row_str)):
        if(row_str[i] == 'B'):
    #        print(2**(len(row_str) - i - 1))
            row_num += (2**(len(row_str) - i - 1))
    #print(row_num)

    #print(col_str)
    for i in range(len(col_str)):
        if(col_str[i] == 'R'):
    #        print(2**(len(col_str) - i - 1))
            col_num += (2**(len(col_str) - i - 1))
    #print(col_num)

    holder = (row_num * 8) + col_num
    #print(str(holder) + '||' + str(highest_number))
    #print('=====================================================================================')

    if(holder > highest_number):
        highest_number = holder
        highest_str = line.strip()

print('=====================================================================================')
print(highest_number)
print(highest_str)
print('=====================================================================================')

end = time.time()
print("Time Elapsed: " + str(end - start))