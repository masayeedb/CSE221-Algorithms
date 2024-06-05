#Task 2

input_data = open("input2.txt", "r")
output_data = open("output2.txt", "w")

line1 = int(input_data.readline())
arr = list(map(int, input_data.readline().split()))

def max_val(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left+right)//2

    l1 = max_val(arr, left, mid)
    l2 = max_val(arr, mid+1, right)
    return max(l1, l2)

ans = max_val(arr, 0, line1-1)
output_data.write(str(ans)+" ")
output_data.close()