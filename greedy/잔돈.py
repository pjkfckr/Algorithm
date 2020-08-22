"""
당장 좋은 것만 선택하는 그리디
현재 상황에서 지금 당장 좋은 것만 고르는 방법
"""
import time
money = 1260

n = [500, 100, 50, 10]
print(money % 500)
count = 0
for i in n:
    start = time.time()
    count += money // i
    print("Count = ", count)
    money %= i
    print("N = ", money)
    end = time.time()
    print(end-start)



