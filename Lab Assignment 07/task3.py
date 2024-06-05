#Task 3

def ways(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

input_data = open("input3.txt", "r")
output_data = open("output3.txt", "w")

N = int(input_data.readline())
output_data.write(str(ways(N)))

input_data.close()
output_data.close()