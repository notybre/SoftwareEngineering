from triangle import heron_area
if __name__ == "__main__":
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    c = float(input("Введите сторону c: "))
    area = heron_area(a,b,c)
    print("Площадь треугольника:", area)
