n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n]
second = data[n-1]

count = int(m / (k + 1)) * k
count += m % (k + 1)


result = 0
result += (count) * first
result += (m - count) * second


print(result)