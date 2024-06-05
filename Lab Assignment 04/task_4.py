#Task 4

input_data = open("input4.txt", "r")
output_data = open("output4.txt", "w")

line1 = input_data.readline().split()
lis = []
dict = {}

def cycle_det(graph, city, visited, stack):
    visited.add(city)
    stack.add(city)
    if city in graph:
        for neighbor in graph[city]:
            if neighbor not in visited:
                if cycle_det(graph, neighbor, visited, stack):
                    return True
            elif neighbor in stack:
                return True
    stack.remove(city)
    return False


def cycle_check(graph):
    visited = set()
    stack = set()
    for i in list(graph.keys()):

        if cycle_det(graph, i, visited, stack):
            return True
    return False



for i in range(int(line1[1])):
    k = input_data.readline().split()
    lis.append(k)
    if lis[i][0] not in dict:
        dict[lis[i][0]] = [lis[i][1]]
    else:
        dict[lis[i][0]].append(lis[i][1])

cycle = cycle_check(dict)
if cycle == True:
    output_data.write("YES")
elif cycle == False:
    output_data.write("NO")
output_data.close()