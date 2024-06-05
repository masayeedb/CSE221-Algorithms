#Task 1b

input_data = open("input1b.txt", "r")
output_data = open("output1b.txt", "w")

n, e = map(int, input_data.readline().split())
course = [tuple(map(int, input_data.readline().split())) for i in range(e)]

def bfs_seq(n, course):
    graph = {}
    inorder = [0]*(n+1)
    for i in range(1, n + 1):
        graph[i] = []

    for prereq in course:
        graph[prereq[0]].append(prereq[1])
        inorder[prereq[1]] += 1

    queue = []
    result = []
    for i in range(1, n+1):
        if inorder[i] == 0:
            queue.append(i)

    while queue:
        course = queue.pop(0)
        result.append(course)

        for n_course in graph[course]:
            inorder[n_course] -= 1
            if inorder[n_course] == 0:
                queue.append(n_course)


    if len(result) == n:
        result = [str(i) for i in result]
        st = " ".join(result)
        output_data.write(st)
        return str(result)[1:len(result)+1]

    else:
        output_data.write("IMPOSSIBLE")

bfs_seq(n, course)

output_data.close()