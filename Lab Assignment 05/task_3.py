#Task 3

input_data = open('input3.txt', 'r')
output_data = open('output3.txt', 'w')

line1 = input_data.readline().split()
dic = {}
lis = []

def dfs(graph, current, visited, stack):
    visited.append(current)
    if current in graph:
        for adjacent in graph[current]:
            if adjacent not in visited:
                dfs(graph, adjacent, visited, stack)
        stack.append(current)


def dfs_scc(graph, current, visited, scc):
    visited.append(current)
    scc.append(current)

    if current in graph:
        for adjacent in graph[current]:
            if adjacent not in visited:
                dfs_scc(graph, adjacent, visited, scc)

def inverse(graph):
    graphU = {}
    n = max(graph.keys())
    for k in graph.keys():
        for v in graph[k]:
            if v not in graphU:
                graphU[v] = [k]
            else:
                graphU[v].append(k)
    return graphU


def scc(graph):
    visited = []
    stack = []

    for node in graph.keys():
        if node not in visited:
            dfs(graph, node, visited, stack)

    inverted = inverse(graph)
    visited = []
    scc_visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs_scc(inverted, node, visited, scc)
            scc_visited.append(scc)

    return scc_visited

for i in range(int(line1[1])):
    k = input_data.readline().split()
    lis.append(k)
    if lis[i][0] not in dic:
        dic[lis[i][0]] = [lis[i][1]]
    else:
        dic[lis[i][0]].append(lis[i][1])

scc = scc(dic)
for i in scc:
    output_data.write(" ".join(i)+" \n")

output_data.close()