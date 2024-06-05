#Task 1b

input_data = open('input1b.txt', 'r')
output_data = open('output1b.txt', 'w')
s = input_data.readline().split()
lis = []
dic = {}

for i in range(int(s[1])):
    k = input_data.readline().split()
    lis.append(k)
    if lis[i][0] not in dic:
        dic[lis[i][0]] = [(int(lis[i][1]), int(lis[i][2]))]
    else:
        dic[lis[i][0]].append((int(lis[i][1]), int(lis[i][2])))

for i in range(int(s[0])):
    if str(i) not in dic:
        print()
        output_data.write(f"{i}:\n")
    else:
        l1 = str(dic[str(i)])
        l1 = l1[1:len(l1)-1]

        output_data.write(f"{i}: {l1}\n")
output_data.close()