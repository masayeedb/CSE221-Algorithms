# Task 1_2

input_data = open("input1_2.txt","r")
output_data = open("output1_2.txt","w")

n,s = map(int,input_data.readline().split(" "))

array = input_data.readline().split(" ")
array = list(map(int, array))

flag = False

for i in range(n):
  if array[i] + array[n-1] == s:
    output_data.write(str(i+1)+" "+ str(n))
    flag = True
    break

if flag == False:
  output_data.write("IMPOSSIBLE")

output_data.close()
