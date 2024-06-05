#Task 3

input_data = open("input3.txt","r")
output_data = open("output3.txt","w")

line1 = int(input_data.readline())

array = input_data.readline().split(" ")
array = list(map(int, array))

def pair(arr):
  if len(arr) <= 1:
    return arr, 0

  else:
    mid = len(arr) // 2
    l, count_l = pair(arr[:mid])
    r, count_r = pair(arr[mid:])

    sorted_arr, count = merge(l, r)
    total_count = count_l + count_r + count
    return sorted_arr, total_count

def merge(l, r):
  merged = []
  count = 0
  i = 0
  j = 0

  while i < len(l) and j < len(r):
    if l[i] > r[j]:
      merged.append(l[i])
      count += len(r) - j
      i += 1
    else:
      merged.append(r[j])
      j += 1

  merged.extend(l[i:])
  merged.extend(r[j:])
  return merged, count

array, count = pair(array)
output_data.write(str(count))

output_data.close()