#Task 4

input_data = open("input4.txt", "r")
output_data = open("output4.txt", "w")

line1 = int(input_data.readline())
arr = list(map(int, input_data.readline().split()))

def max_sum(arr, start, end):
    if start == end:
        return arr[start], start, start
    mid = (start+end)//2

    left_max, left_i, left_j = max_sum(arr, start, mid)
    right_max, right_i, right_j = max_sum(arr, mid + 1, end)

    max_right_value = 0
    for i in range(mid+1, end+1):
        if arr[i]**2 > max_right_value:
            max_right_value = arr[i]**2