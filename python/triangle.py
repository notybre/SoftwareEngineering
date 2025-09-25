import math

def heron_area(a, b, c):
    p = (a +b+c) / 2             # полупериметр
    return math.sqrt(p*(p-a)*(p-b)*(p-c))  # формула Герона
