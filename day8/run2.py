import time
import copy

def check_commands(command_list):
    acc = 0
    index = 0
    loop = True
    stack = []

    #print("=============================")
    #print("Starting Loop")
    while(loop):
        line = command_list[index]
        #print(line)
        if(index not in stack):
            stack.append(index)
            if(line[0] == 'nop'):
                index += 1
            elif(line[0] == 'acc'):
                acc += line[1]
                index += 1
            elif(line[0] == 'jmp'):
                index += line[1]
        else:
            #print("Loop Detected")
            #print("=============================")
            return False

        if(index == len(command_list)):
            loop = False
    #print("Exit")
    print(acc)
    return True



def get_command_list():
    input = open("input.txt", 'r').readlines()
    lines = []
    for line in input:
        line = line
        parts = line.split(' ')
        action = parts[0]
        value = int(parts[1])
        lines.append([action, value])
    return lines

def main():
    command_list = get_command_list()

    for i in range(len(command_list)):
        command_copy = copy.deepcopy(command_list)
        if(command_copy[i][0] == "jmp"):
            command_copy[i][0] = "nop"
        elif (command_copy[i][0] == "nop"):
            command_copy[i][0] = "jmp"
        else:
            #print("Non Replaceable Command")
            continue
        if(check_commands(command_copy)):
            #print("Value Found, Terminating Loop")
            #print("=============================")
            break
        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Time Elapsed: " + str(end - start))