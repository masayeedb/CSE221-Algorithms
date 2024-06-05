#Task 2

def bubbleSort(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        sort = False
    if sort == True:
      break
  return arr


input_data = open("input2.txt","r")
output_data = open("output2.txt","w")

line1 = int(input_data.readline())

line2 = input_data.readline().split(" ")
line2 = list(map(int, line2))

print(" ".join(str(num) for num in bubbleSort(line2)), file = output_data) # This will merge all the index of the list