"""
이진탐색(binary search) 은 탐색 범위를 절반씩 줄여나가면서 찾는다.
장점 : 빠르고 실제로 사용한다.
단점 : 정렬이 되어 있어야 하고, 만들기도 어렵다.
시간복잡도 : O(log n)
핵심로직 : 중간인덱스값을 구한다.  10억개 -> 5억개 > 2억5천개 -> 1억2천5백개
        10억개에서 9억 6천과 현재 중간값
        0------5-------9.6--10   9.6 > half
        5----7.5----10
        7.5---8.75---10
        8.75---9.6---10
        범위가 절반씩 줄어들면서 찾는다.
"""

arr = [1, 2, 3, 5, 7, 8, 9, 10, 25, 50, 70]

def binarySearch(arr, targetNum):
    start = 0
    end = len(arr) - 1
    midindex = len(arr) // 2
    indexvalue = arr[midindex]
    if indexvalue == targetNum:
        return midindex
    elif indexvalue < targetNum:
        start = midindex + 1
    elif indexvalue > targetNum:
        end = midindex - 1
    elif arr[start] == targetNum:
        return arr[start]
    return -1


def pick2(arr):
    index_list = []
    for indexlv1 in range(0, len(arr)):
        for indexlv2 in range(indexlv1 + 1, len(arr)):
            index_list.append((arr[indexlv1], arr[indexlv2]))
    return index_list


if __name__ == '__main__':
    print("Test : ", binarySearch(arr, 9))
    print("pick2 :", pick2(arr))
