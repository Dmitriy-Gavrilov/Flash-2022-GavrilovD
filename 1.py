f = open('1.txt')
N = int(f.readline())
m = sorted(list(map(int, f.read().split())), reverse=True)
count = 0
minn = 100
s, ind = 0, 0

for i in m:
    if (s + i) / (count + 1) >= 90:
        s += i
        count += 1
        minn = i
    else:
        ind = m.index(i)
        break

for i in range(ind + 1, len(m)):
    if (s - minn + m[i]) / count >= 90:
        minn = m[i]

print(count, minn)
