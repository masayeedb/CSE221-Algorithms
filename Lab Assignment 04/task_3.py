#Task 3

input_data = open('input3.txt', 'r')
output_data = open('output3.txt', 'w')

line1 = input_data.readline().split()
lis = []
dic = {}

def dfs(graph, current, visited):
    if current not in visited:
        output_data.write(str(current)+" ")
        visited.add(current)
        if current in graph:
            for adjacent in graph[current]:
                dfs(graph, adjacent, visited)

for i in range(int(line1[1])):
    k = input_data.readline().split()
    lis.append(k)
    if lis[i][0] not in dic:
        dic[lis[i][0]] = [lis[i][1]]
    else:
        dic[lis[i][0]].append(lis[i][1])
    if lis[i][1] not in dic:
        dic[lis[i][1]] = [lis[i][0]]
    else:
        dic[lis[i][1]].append(lis[i][0])
start = list(dic.keys())[0]
visited = set()
print(dfs(dic, start, visited))
output_data.close()