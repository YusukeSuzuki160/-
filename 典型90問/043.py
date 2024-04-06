from collections import deque

h, w = map(int, input().split(" "))
r_s, c_s = map(int, input().split(" "))
r_t, c_t = map(int, input().split(" "))
s = [input() for _ in range(h)]

deq = deque()
deq.append((r_s - 1, c_s - 1, 0))
deq.append((r_s - 1, c_s - 1, 1))
deq.append((r_s - 1, c_s - 1, 2))
deq.append((r_s - 1, c_s - 1, 3))
dist = [[[float("inf") for _ in range(4)] for _ in range(w)] for _ in range(h)]
dist[r_s - 1][c_s - 1][0] = 0
dist[r_s - 1][c_s - 1][1] = 0
dist[r_s - 1][c_s - 1][2] = 0
dist[r_s - 1][c_s - 1][3] = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while deq:
    r, c, d = deq.popleft()
    for i, (dr, dc) in enumerate(directions):
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= h or nc < 0 or nc >= w:
            continue
        if s[nr][nc] == "#":
            continue
        if i == d:
            if dist[nr][nc][d] > dist[r][c][d]:
                dist[nr][nc][d] = dist[r][c][d]
                deq.appendleft((nr, nc, d))
        else:
            if dist[nr][nc][i] > dist[r][c][d] + 1:
                dist[nr][nc][i] = dist[r][c][d] + 1
                deq.append((nr, nc, i))

print(min(dist[r_t - 1][c_t - 1]))