from collections import deque

h, w = map(int, input().split(" "))
r_s, c_s = map(int, input().split(" "))
r_t, c_t = map(int, input().split(" "))
r_s-=1
c_s-=1
r_t-=1
c_t-=1
s = [input() for _ in range(h)]

class State:
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d

deq = deque()
deq.append(State(r_s, c_s, 0))
deq.append(State(r_s, c_s, 1))
deq.append(State(r_s, c_s, 2))
deq.append(State(r_s, c_s, 3))
dist = [[[float("inf") for _ in range(4)] for _ in range(w)] for _ in range(h)]
dist[r_s][c_s][0] = 0
dist[r_s][c_s][1] = 0
dist[r_s][c_s][2] = 0
dist[r_s][c_s][3] = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while deq:
    u = deq.popleft()
    r = u.r
    c = u.c
    d = u.d
    for i in range(4):
        dr = dx[i]
        dc = dy[i]
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= h or nc < 0 or nc >= w:
            continue
        if s[nr][nc] == "#":
            continue
        old_dist = dist[nr][nc][i]
        new_dist = dist[r][c][d] + (1 if i != d else 0)
        if i != d:
            if new_dist < old_dist:
                dist[nr][nc][i] = new_dist
                deq.append(State(nr, nc, i))
        else:
            if new_dist < old_dist:
                dist[nr][nc][i] = new_dist
                deq.appendleft(State(nr, nc, i))

print(min(dist[r_t][c_t]))