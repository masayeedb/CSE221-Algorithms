#Task 5

input_data = open('input5.txt', 'r')
output_data = open('output5.txt', 'w')

line1 = input_data.readline().split()
lis = []
dic = {}

def short(graph, vertex, arr, city):
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
                    arr[int(adjacent)] = current
                    queue.append(adjacent)
    i = int(city)
    k = ""
    count = -1

    while int(i) > 0:
        k += f" {i}"
        i = int(arr[i])
        count += 1
    k = k[::-1]
    output_data.write(f"Time {count} \nShortest Path:{k}")
    return queue, arr


for i in range(int(line1[1])):
    k = input_data.readline().split()
    lis.append(k)
    if int(lis[i][0]) not in dic:
        dic[int(lis[i][0])] = [int(lis[i][1])]
    else:
        dic[int(lis[i][0])].append(int(lis[i][1]))
    if int(lis[i][1]) not in dic:
        dic[int(lis[i][1])] = [int(lis[i][0])]
    else:
        dic[int(lis[i][1])].append(int(lis[i][0]))
print(dic)
start = list(dic.keys())[0]
print(short(dic, start, [0]*(int(line1[0])+1), line1[2]))
output_data.close()