#Task 1a

input_data = open('input1a.txt', 'r')
output_data = open('output1a.txt', 'w')

line1 = input_data.readline().split("\n")

matrix = line1[0].split(' ')
vertices = int(matrix[0])
edges = int(matrix[1])
adj_mat = []

for i in range(vertices+1):
    adj_mat1 = [0]*(vertices+1)
    adj_mat.append(adj_mat1[:])

for j in range(edges):
    st, end, weight = [int(i) for i in input_data.readline().split(' ')]
    adj_mat[st][end] = weight

for i in range(vertices+1):
    for j in range(vertices+1):
        output_data.write(f'{adj_mat[i][j]} ')
    output_data.write('\n')

output_data.close()