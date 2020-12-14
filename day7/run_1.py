import time
def update_bag_list(bag_list, gold_bag_list):
    new_gold_list = []
    gold_bags = 0

    print("========================")
    print("Bag List: ")
    for entry in bag_list:
        print(entry)
        contains_gold_bag = check_bag(entry, bag_list, gold_bag_list)
        if(contains_gold_bag):
            new_gold_list.append(entry)
            gold_bags += 1
    print("========================")

    if(new_gold_list != []):
        print("========================")
        print("New Gold List: ")
        for entry in new_gold_list:
            print(entry)
            bag_list.pop(entry)
        print("========================")
        gold_bags += update_bag_list(bag_list, new_gold_list)
    
    return gold_bags

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
bag_count = 0

gold_bag_list = []
other_bag_list = {}

while(loop):

    parts = line.split('contain')
    bag_name = parts[0].strip()
    contents = {}
    contains_gold_bag = False

    for entry in parts[1].split(','):
        entry = entry.strip()
        if(entry[0].isdigit()):
            if(entry[2:] == 'shiny gold'):
                contains_gold_bag = True
                break
            else:
                contents[entry[2:]] = int(entry[0])

    if(contains_gold_bag):
        gold_bag_list.append(bag_name)
        bag_count += 1
    else:
        other_bag_list[bag_name] = contents

    line = input.readline().strip().replace('bags', '').replace('bag', '')[:-1]
    if(line == ''):
        loop = False

bag_count += update_bag_list(other_bag_list, gold_bag_list)

print(bag_count)

end = time.time()
print("Time Elapsed: " + str(end - start))