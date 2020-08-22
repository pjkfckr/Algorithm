# 버블 정렬

"""
핵심로직
첫번째 값 과 두번째 값 비교해서 두번째 값이 더 작으면
첫번째 값과 자리를 바꾼다.
n, n+1 => 권위주위의 상징
"""

numbers = [7,1,3, 2,2, 89,9, 4, 10, 20, 30] # n = 1
    #[3, 7, 2, 9]
    #[2, 7, 3, 9]
    #[2, 7, 3, 9]

# 0번째와 나머지를 모두 비교를 한다.  1바퀴
# 가장 작은게 0번째에 온다.
# 그 다음으로 작은게 1번째에 오게 해야 한다.



def bubble(array):
    for i in range(0, len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            print(array)

    return array


if __name__ == '__main__':
    print("Test : ", bubble(numbers))





