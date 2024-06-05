#Task 1_1

input_data = open("input1_1.txt", "r")
output_data = open("output1_1.txt", "w")

line1 = input_data.readline().split()
n, s = [int(i) for i in line1]

line2 = input_data.readline().split()
line2 = [int(i) for i in line2]

flag = False
for i in range(n):
    if flag == False:
        for j in range(i+1,n):
            if i != j:
                if line2[i] + line2[j] == s:
                    output_data.write(str(i+1)+" "+str(j+1))
                    flag = True
                    break
    else:
        break

if flag == False:
    output_data.write("impossible")

output_data.close()