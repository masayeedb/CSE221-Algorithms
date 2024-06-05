#Task 3

input_data = open('input3.txt','r')
output_data = open('output3.txt','w')

line1 = input_data.readline()

line2 = input_data.readline().split()
line2 = [int(i) for i in line2]

line3 = input_data.readline().split()
line3 = [int(i) for i in line3]

for i in range(len(line2)-1):
  temp = i
  for j in range(i+1,len(line2)):
      if line3[temp] < line3[j]:
        line3[temp],line3[j] = line3[j],line3[temp]
        line2[temp],line2[j] = line2[j],line2[temp]

      elif line3[temp] == line3[j]:
        if line2[temp] > line2[j]:
          line2[temp],line2[j] = line2[j],line2[temp]

for i in range(len(line2)):
  print(f"ID: {str(line2[i])} Mark: {str(line3[i])}", file = output_data)
