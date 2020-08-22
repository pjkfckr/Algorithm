## 토큰(Token)이란?
"""
프로그램에서 다루는 최소 단위
ex) 이름 박상영을 다룰 때 박은 성이고 상영은 이름이다.
이 각각을 토근이라고 한다.
"""

## Tokenizer란?
"""
가장 작은 단위로 나누어 주는 일을 하는게 토크나이저다.
"""

## 왜 나눠서 처리하느냐?
# 나눠서 처리 해야 하기 때문

## StringTokenizer란?
"""
String 을 나누어 주는 로직이 String Tokenizer 이다.
"""

str = "13+3*{24*(35-46.76)-89}"
# 1 + (2 * 3) - (2 * 4)
# 1 + (6) - (8)
# 1 + (-2)
# -1

# 숫자와 괄호를 분리 해주는 식

def stringTokenizer(string, deli):
    """
    1, +, 2, *, (, 3, -, 4, )
    """
    result = list()
    accu = ""
    for char in string:
        if char in "+-*/(){}[]^":
            if accu != "":
                result.append(accu)
                accu = ""
            result.append(char)
        else:
            accu = accu + char
    return result
result = stringTokenizer(str, "+-*/(){}[]^")
print("result => ", result)