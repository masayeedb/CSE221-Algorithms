#Task 1

input_data = open("input1.txt", "r")
output_data = open("output.txt", "w")

def kripon(graph, source):
    distances = [-1]*len(graph)
    distances[source-1] = 0

    priority_queue = [(source, 0)]

    while priority_queue:
        u, d = priority_queue.pop(0)
        if u in graph:
            for v, weight in graph[u]:
                sum = d+weight
                if distances[v-1] == -1 or distances[v-1] > sum:
                    distances[v-1] = sum
                    priority_queue.insert(0, (v, weight))

    return distances

lines = input_data.readline()
n, e = map(int, lines.split())
graph = {}
for i in range(e):
    u, v, w = map(int, input_data.readline().split())
    if u not in graph:
        graph[u] = [(v, w)]
    else:
        graph[u].append((v, w))

source = int(input_data.readline().strip())

start_b_line = input_data.readline().strip()
start_b = int(start_b_line) if start_b_line else None

distances = kripon(graph, source)
output_data.write(" ".join(map(str, distances)))