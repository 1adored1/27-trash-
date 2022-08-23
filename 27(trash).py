f = open('27.txt')
n = int(f.readline())

a = []
for i in range(n):
    a.append(int(f.readline()))

# сумма если завод на нулевой позиции
sums = [0] * n
for i in range(n):
    sums[0] += a[i] * min(i, n - i)

s_l = sum(a[n // 2 + 1:]) + a[0]  # сумма чисел слева от диаметра на нулевой позиции
s_r = sum(a[1:n // 2 + 1])  # сумма чисел справа от диаметра на нулевой позиции
mn = float('inf')

for i in range(1, n):
    sums[i] += sums[i - 1] + s_l - s_r  # изменение суммы нынешней позиции
    s_l += a[i] - a[(n // 2 + i) % n]  # изменение суммы числе слева от диаметра
    s_r += a[((n // 2 + i) % n)] - a[i]  # изменение суммы чисел справа от диаметра
    if sums[i] < mn:
        mn = sums[i]
        counter = i + 1
print(counter)
