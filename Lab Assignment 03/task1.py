#Task 1

input_data = open("input1.txt", "r")
output_data = open("output1.txt", "w")

line1 = input_data.readline().split()
arr = list(map(int, input_data.readline().split()))

def merge(l1, l2):
    l = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):

        if int(l1[i]) <= int(l2[j]):
            l.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            l.append(l2[j])
            j += 1

    while i < len(l1):
        l.append(l1[i])
        i += 1
    while j < len(l2):
        l.append(l2[j])
        j += 1
    return l


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[0:mid])
        a2 = mergeSort(arr[mid:len(arr)])
        return merge(a1, a2)

arr = mergeSort(arr)
for i in arr:
    output_data.write(str(i)+" ")
output_data.close()