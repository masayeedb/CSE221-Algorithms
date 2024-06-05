#Task 1a
input_data = open("input1a.txt", "r")
output_data = open("output1a.txt", "w")

# This will read the first line
line1 = int(input_data.readline())

for i in range(line1):
    # This will read from line 2 to line 5
    num = int(input_data.readline())

    if num % 2  == 0:
        print(f"{num} is an Even number", file = output_data)
    else:
        print(f"{num} is an Odd number", file = output_data)
