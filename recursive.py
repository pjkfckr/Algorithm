# 재귀(recursive)
# 재귀는 자기 자신을 호출 하는 것을 말합니다.

## 재귀함수(recursive function)
## 재귀함수는 자기 자신을 호출하는 함수 입니다.

## 재귀함수 만들기
## 탈출조건, 끝나는 조건이 꼭 들어가야 한다.

arr = [7, 3, 2, 9]

def sum_array(array, accu):
    if (len(array) == 0): return accu
    return sum_array(array, accu + array.pop())


result = sum_array(arr, 0)
print(result)

