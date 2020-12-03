content = open("input.txt", 'r').readlines()
holder = []
for line in content:
    holder.append(int(line[:-1]))


for i in range(len(holder)):
    for j in range(i, len(holder)):
        for k in range(j, len(holder)):
            if(holder[i] + holder[j] + holder[k] == 2020):
                print(holder[i])
                print(holder[j])
                print(holder[k])
                print(holder[i] * holder[j] * holder[k])
