graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    stack = [start]
    visited = set()
    path = []

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue

        visited.add(vertex)
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

print(bfs(graph,'A'))

