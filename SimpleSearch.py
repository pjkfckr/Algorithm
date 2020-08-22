"""
단순탐색(Simple Search)은 앞에서부터 원하는게 나올 때까지 하나하나 찾는다.
장점 : 만들기 쉽고 정렬이 안되어있어도 된다.
단점 : 느리다. 10억개에서 찾을시 10억번이 돌수도있다.
시간복잡도 : O(n)
대안 : 이진탐색(Binary Search) O(log n) 10억개에서 찾을시 2x번
"""
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def simpleSearch(arr, targetNum):
    for index in range(0, len(arr)):
        if arr[index] == targetNum:
            return index
    return -1

if __name__ == '__main__':
    print("Test : ", simpleSearch(arr, 8))
    print("Test : ", simpleSearch(arr, 3))
