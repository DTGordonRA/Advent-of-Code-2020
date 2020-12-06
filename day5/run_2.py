import time
start = time.time()

# def mergeSort(baselist):
#     mid = len(baselist) // 2
#     left_half = baselist[:mid]
#     right_half = baselist[mid:]

#     mergeSort(left_half)
#     mergeSort(right_half)

#     left_iter = 0
#     right_iter = 0
#     main_iter = 0
#     while left_iter < len(left_half) and right_iter < len(right_half):
#         if left_half[left_iter] < right_half[right_iter]:
#             baselist[main_iter] = left_half[left_iter]
#             left_iter += 1
#         else:
#             baselist[main_iter] = right_half[right_iter]
#             right_iter += 1
#         main_iter += 1

#     while left_iter < len(left_half):
#         baselist[main_iter] = left_half[left_iter]
#         main_iter += 1
#         left_iter += 1

#     while right_iter < len(right_half):
#         baselist[main_iter] = right_half[right_iter]
#         main_iter += 1
#         right_iter += 1


data = open("input.txt", 'r').readlines()

highest_number = 0
highest_str = ''

lowest_number = (2**7 - 1) * 8 + 7
lowest_str = ''

seating_map = []


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
    elif(holder < lowest_number):
        lowest_number = holder
        lowest_str = line.strip()

    seating_map.append(holder)

print('=====================================================================================')
print(highest_number)
print(highest_str)
print(lowest_number)
print(lowest_str)
print('=====================================================================================')
midpoint = (int)((highest_number + lowest_number) / 2)
# print(midpoint)
# print(seating_map[midpoint])

# print('=====================================================================================')
# mergeSort(seating_map)
# print(seating_map)
# print('=====================================================================================')
for i in range(0, len(seating_map) - 1):
    for j in range(0, len(seating_map) - 1):
        if(seating_map[j] > seating_map[j + 1]):
            # Single line swap
            seating_map[j], seating_map[j + 1] = seating_map[j + 1], seating_map[j]

start = seating_map[0]
for i in range(len(seating_map) - 1):
    if((seating_map[i] + 1) != seating_map[i+1]):
        print(seating_map[i] + 1)

end = time.time()
print("Time Elapsed: " + str(end - start))