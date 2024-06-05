#Task 2

input_data = open('input2.txt', 'r')
output_data = open('output2.txt', 'w')

line1 = input_data.readline().split()
lis = []
dic = {}

def bfs(graph, vertex):
    visited = set()
    visited.add(vertex)
    queue = [vertex]
    while queue:
        current = queue.pop(0)
        output_data.write(str(current)+" ")
        if current in graph:
            for adjacent in graph[current]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(adjacent)

    return queue

for i in range(int(line1[1])):
    k = input_data.readline().split()
    lis.append(k)
    if lis[i][0] not in dic:
        dic[lis[i][0]] = [lis[i][1]]
    else:
        dic[lis[i][0]].append(lis[i][1])
start = list(dic.keys())[0]
print(bfs(dic, start))
output_data.close()