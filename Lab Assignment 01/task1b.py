#Task 1b

input_data = open("input1b.txt","r")
output_data = open("output1b.txt", "w")

# This will read the first line
line1 = int(input_data.readline())

for i in range(line1):
    # This will read from line 2 to line 15
    line = input_data.readline()
    lis = line.split()

    if lis[2] == "+":
        result = int(lis[1]) + int(lis[3])
        print(f"The result of {lis[1]} {lis[2]} {lis[3]} is {result}", file = output_data)
    elif lis[2] == "-":
        result = int(lis[1]) - int(lis[3])
        print(f"The result of {lis[1]} {lis[2]} {lis[3]} is {result}", file = output_data)
    elif lis[2] == "*":
        result = int(lis[1]) * int(lis[3])
        print(f"The result of {lis[1]} {lis[2]} {lis[3]} is {result}", file = output_data)
    elif lis[2] == "/":
        result = int(lis[1]) / int(lis[3])
        print(f"The result of {lis[1]} {lis[2]} {lis[3]} is {result}", file = output_data)
