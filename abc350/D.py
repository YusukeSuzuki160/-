class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]


n, m = map(int, input().split(" "))
if m == 0:
    print("0")
    exit()
a = []
b = []

for _ in range(m):
    a_in, b_in = map(int, input().split(" "))
    a.append(a_in)
    b.append(b_in)

uf = UnionFind(n)

for i in range(m):
    _a = a[i]
    _b = b[i]
    uf.unite(_a - 1, _b - 1)

ans = 0

for i in uf.roots():
    size = uf.size(i)
    ans += size * (size - 1) // 2

print(ans - m)