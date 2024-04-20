def dfs(graph, distances, start):
    stack = [start]
    visited = [False for _ in range(len(graph))]
    visited[start] = True
    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                distances[neighbor] = distances[current] + 1

n = int(input())
graph = [[] for _ in range(n)]
distances = [0 for _ in range(n)]
for i in range(n - 1):
    a_, b_ = map(int, input().split(" "))
    graph[a_ - 1].append(b_ - 1)
    graph[b_ - 1].append(a_ - 1)

dfs(graph, distances, 0)
max_distance_index = distances.index(max(distances))
distances = [0 for _ in range(n)]
dfs(graph, distances, max_distance_index)
print(max(distances) + 1)