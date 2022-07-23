f = open('2.txt')
N, M = list(map(int, f.readline().split()))
m = sorted(list(map(int, f.read().split())), reverse=True)
m1 = m.copy()
ans, isp = [], []
mins = 100000

for i in m:
    if m.count(i) == isp.count(i):
        continue
    k = [i]
    for j in m1:
        if k[0] > j and k[0] + j <= M:
            k.append(j)
            break
    isp += k
    ans.append(k)
    for g in k:
        del m1[m1.index(g)]

count = len(ans)
ans1 = sorted(list(filter(lambda x: len(x) == 1, ans)))[0][0]
ans2 = sorted(list(filter(lambda x: len(x) == 2, ans)))
for i in ans2:
    if ans1 > i[1] and ans1 + i[1] <= M:
        mins = min(ans1 + i[1], mins)

print(count, mins)
