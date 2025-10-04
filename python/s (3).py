import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def heron(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(max(0, s*(s-a)*(s-b)*(s-c)))
    return area
#реугольник из максимальных сторон
a_max, b_max, c_max = max(one), max(two), max(three)
area_max = heron(a_max, b_max, c_max)
#Треугольник из минимальных сторон
a_min, b_min, c_min = min(one), min(two), min(three)
area_min = heron(a_min, b_min, c_min)
print("Стороны (max):", (a_max, b_max, c_max), "Площадь: ", area_max)
print("Стороны (min): ", (a_min, b_min, c_min), "Площадь:", area_min)
