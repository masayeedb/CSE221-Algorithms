#Task 4

input_data = open('input4.txt','r')
output_data = open('output4.txt','w')

s=input_data.readline().split()

s1=[int(i) for i in s]

lis = []

for i in range(s1[0]):
     s=input_data.readline().split()
     s=[int(i) for i in s]
     lis.append(s)

for i in range(len(lis)-1):
    min_id=i
    for j in range(i+1,len(lis)):
            if lis[min_id][1]>lis[j][1]:
                lis[min_id],lis[j]=lis[j],lis[min_id]
count = 1
new = lis[0][1]
lis1 = []


lis1.append(lis[0])


for i in range(s1[1]):

  temp = 1
  for j in range(s1[0]):


    if  lis[j][0] >= new and lis[j][0] not in lis1:
      if len(lis1)>=2 and lis[j] not in lis1:
        if  (abs(lis1[-2][1]-lis[temp][0]) < abs(lis1[-2][1]-lis1[-1][0])):
          lis1.pop()
          lis1.append(lis[temp])
      lis1.append(lis[j])
      new = lis[j][0]
      temp+=1

    if temp >= len(lis)-1:
      temp = 1

    temp += 1
output_data.write(f"{temp}")
output_data.close()