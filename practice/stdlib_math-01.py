import math

# 피타고라스 정리를 사용해서 두점 사이의 거리를 구하기
# define the two points as tuples
point1 = (3, 4)
point2 = (6, 8)

# calculate the distance using the distance formula
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# print the distance
print("The distance between point 1 and point 2 is", distance)