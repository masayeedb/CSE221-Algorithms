#Task 2_2

input_data=open("input2_2.txt","r")
output_data=open('output2_2.txt','w')

s=input_data.readline()

line1=input_data.readline().split()
line1=[int(i) for i in line1]

s=input_data.readline()

line2=input_data.readline().split()
line2=[int(i) for i in line2]

def merge(line1, line2):
    l = []
    i = 0
    j = 0
    m = 0
    k = 0
    if len(line1) > len(line2):
        m = len(line2)
    else:
        m = len(line1)
    while k<= m:
        if line1[i] < line2[j]:
            l.append(line1[i])
            i += 1

            k += 1
        elif line1[i] > line2[j]:

            l.append(line2[j])
            j += 1
            k += 1

        else:
            l.append(line1[i])
            i += 1
            k += 1

    if i+1 >= len(line1):
        l += line2[j:]
    elif j+1 >= len(line2):
        l += line1[i:]

    for i in l:
      output_data.write(f"{i} ")
    output_data.close()
    return

merge(line1, line2)