class ppr(object) :
    def __init__(self, b, g):
        self.b = b
        self.g = g
    def getb(self):
        return self.b
    def getg(self):
        return self.g

n = int(input())
t = []
for i in range(n):
    l, r = map(int, input().split())
    tmp=ppr(l, r)
    t.append(tmp)
t.sort(key=ppr.getb)
bb = t[0].getb()
gg = t[0].getg()
m1 = bb-gg
m2 = 0
for i in range(1, n):
    if t[i].getb() > gg:
        print("%d %d" % (bb, gg))
        bb = t[i].getb()
        gg = t[i].getg()
    else:
        gg = max(gg, t[i].g)
print("%d %d" % (bb, gg))
