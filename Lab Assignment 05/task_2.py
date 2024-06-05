#Task 2

input_data = open("input2.txt", "r")
output_data = open("output2.txt", "w")
n, e = map(int, input_data.readline().split())

dic = {}
lis = []

def dfs_seq(course, prereq, visited, indegree, result):
    if course not in visited:
        visited.append(course)
        result.append(course)

    if course in prereq:
        for neighbor in prereq[course]:
            indegree[int(neighbor)] -= 1
            if indegree[int(neighbor)] == 0 and neighbor not in visited:
                dfs_seq(neighbor, prereq, visited, indegree, result)

def dfs_course_seq(n, prereq):
    result = []
    visited = []
    indegree = [0]*(n+1)
    for neighbors in prereq.values():
        for neighbor in neighbors:
            indegree[int(neighbor)] += 1

    for course in prereq.keys():
        if indegree[int(course)] == 0 and course not in visited:
            dfs_seq(course, prereq, visited, indegree, result)

    if len(result) == n:
        output_data.write(" ".join(result))

    else:
        output_data.write("IMPOSSIBLE")

for i in range(e):
    k = input_data.readline().split()
    lis.append(k)

    if lis[i][0] not in dic:
        dic[lis[i][0]] = [lis[i][1]]
    else:
        dic[lis[i][0]].append(lis[i][1])

dfs_course_seq(n, dic)

output_data.close()