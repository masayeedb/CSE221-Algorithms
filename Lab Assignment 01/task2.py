# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b-huQVlapQ3yaBfKr_L3-59nfG-vz2H_
"""

#Task 2

def bubbleSort(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        sort = False
    if sort == True:
# If we have to sort the array using bubble sort then we have to run both outer and inner loop and the time complexity 0(n^2). We have to break the loop if the given array was already sorted.Therefore, the time complexity will be 0(n).
      break
  return arr


input_data = open("input2.txt","r")
output_data = open("output2.txt","w")

line1 = int(input_data.readline())

line2 = input_data.readline().split(" ")
# This will Convert the string to int.
line2 = list(map(int, line2))

print(" ".join(str(num) for num in bubbleSort(line2)), file = output_data) # This will merge all the index of the list