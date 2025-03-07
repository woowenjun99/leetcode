class FTree:
    def __init__(self, f):
        self.n = len(f)
        self.ft = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.ft[i] += f[i - 1]
            if i + self.lsone(i) <= self.n:
                self.ft[i + self.lsone(i)] += self.ft[i]

    def lsone(self, s):
        return s & (-s)

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)
        return s

    def update(self, i, v):
        while i <= self.n:
            self.ft[i] += v
            i += self.lsone(i)

    def select(self, k):
        p = 1
        while (p * 2) <= self.n: p *= 2

        i = 0
        while p > 0:
            if k > self.ft[i + p]:
                k -= self.ft[i + p]
                i += p
            p //= 2

        return i + 1