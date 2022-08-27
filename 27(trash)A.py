f = open('')
n = int(f.readline())
a = []
for i in range(n):
    x = int(f.readline())
    a.append(x)

sums = [0] * n
mn = float('inf')

# перебор всех возможных вариантов
for i in range(n):
    for j in range(n):
        sums[i] += a[j] * min(abs(i - j), n - abs(i - j))
    if sums[i] < mn:
        mn = sums[i]
        counter = i + 1
print(counter)
