#Task 2

input_data = open("input2.txt", "r")
output_data = open("output.txt", "w")

def mapper(graph, start, n):
    distances = [float('inf')]*(n+1)

    distances[start] = 0
    priority_queue = [(start, 0)]
    while priority_queue:
        u, d = priority_queue.pop(0)
        if u in graph:
            for v, weight in graph[u]:
                sum = d+weight
                if distances[v] == -1 or distances[v] > sum:
                    distances[v] = sum
                    priority_queue.insert(0, (v, sum))
    return distances


def meet_pointer(graph, start_a, start_b, n):

    distances_a = mapper(graph, start_a, n)
    distances_b = mapper(graph, start_b, n)

    min_time = float('inf')
    meet = -1
    for node in range(1, n+1):
        if node != start_a or node != start_b:
            time = max(distances_a[node], distances_b[node])


            if time < min_time:
                min_time = time
                meet = node

    if min_time != float("inf"):
        return f"Time:{min_time}\n", f"Node:{meet}"
    else:
        return "", "IMPOSSIBLE"

line1 = input_data.readline()
n, e = map(int, line1.split())

graph = {}
for i in range(e):
    u, v, w = map(int, input_data.readline().split())
    if u not in graph:
        graph[u] = [(v, w)]
    else:
        graph[u].append((v, w))

start_a, start_b = map(int, input_data.readline().split())

distances = meet_pointer(graph, start_a, start_b, n)
output_data.write(distances[0])
output_data.write(distances[1])