# task5

input_data = open("input5.txt","r")
output_data = open("output5.txt","w")

line1 = int(input_data.readline())

arr = input_data.readline().split(" ")
arr = list(map(int, arr))

def quicksort(a, p, r):
  if p < r:
    q = partition(a, p, r)
    quicksort(a, p, q-1)
    quicksort(a, q+1, r)
  return arr

def partition(a, p, r):
  x = a[r]
  i = p-1
  for j in range(p, r, 1):
    if a[j] < x:
      i += 1
      a[i], a[j] = a[j], a[i]
  a[i+1], a[r] = a[r], a[i+1]
  return i+1


output_data.write(" ".join(str(num) for num in quicksort(arr, 0, line1-1)))
output_data.close()