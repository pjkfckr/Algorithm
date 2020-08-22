a, b = map(int, input().split())

array = [list(map(int, input().split())) for i in range(a)]

min_num = [min(array[j]) for j in range(len(array))]

print(max(min_num))