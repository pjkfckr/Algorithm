# 정렬 - 버블, 선택, 삽입, 병합, 퀵

# 퀵정렬
#[40, 35, 27, 50, 75]
#    27 35 40
#    27 35 40 50 75

# 재귀를 이용해서 남은 애들은 계속 함수를 돌린다.
import time
numbers = [235,1000,24,40, 35, 27, 50, 75, 32, 55, 30, 80, 90, 600, 20, 1, 3, 6, 7, 235, 4, 6,100,530,46,539,43230,439,520]

def quicksort(array):
    start = time.time()
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [number for number in array[1:] if number < pivot]
        greater = [number for number in array[1:] if number > pivot]

    end = time.time()
    print(end - start)
    return quicksort(less) + [pivot] + quicksort(greater)

result = quicksort(numbers)
print(result)