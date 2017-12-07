def get_closest_safe_squares(m, origin):
    """
    Return the nearby safe squares.
    Order it returns will influence DFS
    """

    row = origin[0]
    col = origin[1]
    safe_squares = []
    safe_markers = ['S', 'E']

    if col+1< len(m[0]) and m[row][col+1] in safe_markers:   # Right
        safe_squares.append((row, col+1))
    if row-1 >= 0 and m[row-1][col] in safe_markers:         # Up
        safe_squares.append((row-1, col))
    if col-1 >= 0 and m[row][col-1] in safe_markers:         # Left
        safe_squares.append((row, col-1))
    if row+1 < len(m) and m[row+1][col] in safe_markers:     # Down
        safe_squares.append((row+1, col))

    return safe_squares

def dfs_paths_matrix(matrix, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (coords, path) = stack.pop()
        if coords not in visited:
            if coords == goal:
                return path
            visited.add(coords)
            for neighbor in get_closest_safe_squares(matrix, coords):
                stack.append((neighbor, path + [neighbor]))

m = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ],     # 0
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ],     # 1
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ],     # 2
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ],     # 3
    [' ', ' ', ' ', 'S', 'X', 'X', 'X', 'X', ],     # 4
    ['S', 'S', 'S', 'S', 'X', 'X', 'X', 'X', ],     # 5
    ['S', ' ', 'S', ' ', 'X', 'X', 'X', 'X', ],     # 6
    ['S', 'S', 'S', ' ', 'X', 'X', 'X', 'X', ],     # 7
]

print(dfs_paths_matrix(m,(7,0), (4,3)))