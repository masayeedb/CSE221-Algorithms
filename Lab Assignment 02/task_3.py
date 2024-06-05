#Task 3

input_data = open('input3.txt','r')
output_data = open('output3.txt','w')
s = input_data.readline()

lis = []
for i in range(int(s)):
     s = input_data.readline().split()
     s = [int(i) for i in s]
     lis.append(s)

for i in range(len(lis)-1):
    min_id = i
    for j in range(i+1,len(lis)):
            if lis[min_id][1] > lis[j][1]:
                lis[min_id],lis[j] = lis[j],lis[min_id]

count = 1
new = lis[0][1]
l1 = []
l1.append(lis[0])
for i in range(1,len(lis)):
     if new <= lis[i][0]:
          new = lis[i][1]
          l1.append(lis[i])

          count += 1
output_data.write(f"{str(count)}\n")

for i in range(len(l1)):
     output_data.write(f"{l1[i][0]} {l1[i][1]}\n")

output_data.close()