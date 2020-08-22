
def highFrequencyLetterCount(words):
    # alphabet의 갯수 세
    map = dict()
    for alpha in words:
        if map.get(alpha) == None:
            map[alpha] = 1
        else:
            map[alpha] += 1

    # dict에서 가장 큰 수 찾
    max = -1
    for key, val in map.items():
        if map[key] > max:
            max = map[key]
            print(map)
    return max





if __name__ == '__main__':
    print("Test : ", highFrequencyLetterCount("test"))