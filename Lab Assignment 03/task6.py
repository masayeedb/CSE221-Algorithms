# Task 6

input_data = open("input6.txt","r")
output_data = open("output6.txt","w")

line1 = int(input_data.readline()[0])
arr = input_data.readline().split(" ")
arr = list(map(int, arr))

q = int(input_data.readline()[0])

def partition(a, p, r):
  x = a[r]
  i = p-1
  for j in range(p, r, 1):
    if a[j] < x:
      i += 1
      a[i], a[j] = a[j], a[i]
  a[i+1], a[r] = a[r], a[i+1]
  return i+1

def kth_small(a, k):
  p = 0
  r = len(a)-1
  while p <= r:
    p_index = partition(a, p, r)
    if p_index == k-1:
      return a[p_index]
    elif p_index > k-1:
      r = p_index-1
    else:
      p = p_index+1
  return None

for i in range(q):
  K = int(input_data.readline())
  smallest_num = kth_small(arr, K)
  output_data.write(str(smallest_num)+"\n")

output_data.close()