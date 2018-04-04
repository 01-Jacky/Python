graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

"""
stack: A        pop A and push B C
stack: B C      pop B and push D E (A was already seen)
stack: C D E
....

"""

def dfs_no_path(graph, start, goal):
    stack = []
    visited = set()

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            if node == goal:            # Goal check
                return True

            visited.add(node)           # Mark visited so we don't redo it

            for child in graph[node]:               # add children
                stack.append(child)

    return False

def dfs(graph, start):
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


def dfs_path(graph, start, goal):
    stack = []
    visited = set()

    stack.append((start, [start]))  # Tuple (node, list consisting path to node)

    while stack:
        (node, path) = stack.pop()

        if node not in visited:
            if node == goal:  # Goal check
                return path

            visited.add(node)  # Mark visited so we don't redo it

            for child in graph[node]:  # add children
                stack.append((child, path + [child]))

    return False, None


print(dfs_path(graph,'A','F'))

