
# 피타고라스
# 대각선 = 루트(x축 제곱 + y축 제곱)
# 대각선 = sqrt(x^2 + y^2)
import math

man = (0, 0)
girl = (2, 2)

def get_distance(dot1, dot2):
    x = dot2[0] - dot1[0]
    y = dot2[1] - dot1[1]
    distance = math.pow(x, 2) + math.pow(y, 2)
    return math.sqrt(distance)

result = get_distance(man, girl)
print(result)

class Distance:
    def __inti__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2

    @property
    def distance(self):
        x = dot2[0] - dot1[0]
        y = dot2[1] - dot1[1]
        return x, y

    @distance.setter
    def distance(self, dis):

