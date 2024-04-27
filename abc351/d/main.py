def can_move(s, x, y, h, w):
    if x < 0 or x >= h:
        return False
    if y < 0 or y >= w:
        return False
    if x == 0:
        if y == 0:
            if s[x][y + 1] == "#":
                return False
            if s[x + 1][y] == "#":
                return False
            return True
        if y == w - 1:
            if s[x][y - 1] == "#":
                return False
            if s[x + 1][y] == "#":
                return False
            return True
        if s[x][y - 1] == "#":
            return False
        if s[x][y + 1] == "#":
            return False
        if s[x + 1][y] == "#":
            return False
        return True
    if x == h - 1:
        if y == 0:
            if s[x][y + 1] == "#":
                return False
            if s[x - 1][y] == "#":
                return False
            return True
        if y == w - 1:
            if s[x][y - 1] == "#":
                return False
            if s[x - 1][y] == "#":
                return False
            return True
        if s[x][y - 1] == "#":
            return False
        if s[x][y + 1] == "#":
            return False
        if s[x - 1][y] == "#":
            return False
        return True
    else:
        if y == 0:
            if s[x][y + 1] == "#":
                return False
            if s[x - 1][y] == "#":
                return False
            if s[x + 1][y] == "#":
                return False
            return True
        if y == w - 1:
            if s[x][y - 1] == "#":
                return False
            if s[x - 1][y] == "#":
                return False
            if s[x + 1][y] == "#":
                return False
            return True
        if s[x][y - 1] == "#":
            return False
        if s[x][y + 1] == "#":
            return False
        if s[x - 1][y] == "#":
            return False
        if s[x + 1][y] == "#":
            return False
        return True

def dfs(s, x_s, y_s, visited):
    stack = []
    stack.append((x_s, y_s))
    node_count = 0
    while len(stack) > 0:
        x, y = stack.pop()
        if not visited[x][y] and s[x][y] == ".":
            visited[x][y] = True
            node_count += 1
            indexes = can_move_indexes(s, x, y, h, w)
            for x_, y_ in indexes:
                if visited[x_][y_]:
                    continue
                stack.append((x_, y_))
        
    scores[x_s][y_s] = node_count + 1


h, w = map(int, input().split(" "))
s = [list(input()) for _ in range(h)]
scores = [[0] * w for _ in range(h)]
visited = [[False] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            dfs(s, i, j, visited)

max_score = 0
for i in range(h):
    for j in range(w):
        if scores[i][j] > max_score:
            max_score = scores[i][j]

print(max_score)