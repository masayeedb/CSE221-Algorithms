#Task 2_1

input_data=open("input2_1.txt","r")
output_data=open('output2_1.txt','w')

s = input_data.readline()

line1=input_data.readline().split()
line1=[int(i) for i in line1]

s = input_data.readline()

line2=input_data.readline().split()
line2=[int(i) for i in line2]

def merge(line1,line2):
  l=line1+line2
  l.sort()
  for i in l:
    output_data.write(f"{i} ")
merge(line1,line2)

output_data.close()