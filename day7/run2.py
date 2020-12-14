import time

def get_bag_count(bag, bag_list):
    bag_count = 1
    contents = bag_list[bag]
    for entry in contents:
        # print("========================")
        # print(entry)
        # print(bag_list[bag][entry])
        # print(bag_list[entry])
        # print(bag_count)
        bag_count += bag_list[bag][entry] * get_bag_count(entry, bag_list)
        # print(entry + ": " + str(bag_count))
        # print("========================")
    
    return bag_count


def check_bag(bag, bag_list, gold_bag_list):
    for container in gold_bag_list:
        if container in bag_list[bag]:
            return True
    return False


start = time.time()

input = open("input.txt", 'r')

loop = True
line = input.readline().strip()[:-1]
line = line.replace('bags', '').replace('bag', '')

bag_list = {}

while(loop):

    parts = line.split('contain')
    bag_name = parts[0].strip()
    contents = {}
    contains_gold_bag = False

    for entry in parts[1].split(','):
        entry = entry.strip()
        if(entry[0].isdigit()):
            contents[entry[2:]] = int(entry[0])

    bag_list[bag_name] = contents

    line = input.readline().strip().replace('bags', '').replace('bag', '')[:-1]
    if(line == ''):
        loop = False

# print(bag_list['shiny gold'])
bag_count = (get_bag_count("shiny gold", bag_list) - 1)

print(bag_count)

end = time.time()
print("Time Elapsed: " + str(end - start))