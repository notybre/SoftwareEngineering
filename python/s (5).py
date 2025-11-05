class NegativeValueError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeValueError("Нельзя извлечь корень из отрицательного числа!")
    return x ** 0.5

def factorial(n):
    if n < 0:
        raise NegativeValueError("Факториал отрицательного числа не существует!")
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

if __name__ == '__main__':
    try:
        print("корень 16 =", square_root(16))
        print("корень -4 =", square_root(-4))
    except NegativeValueError as e:
        print("Ошибка:", e)

    try:
        print("5! =", factorial(5))
        print("-3! =", factorial(-3))
    except NegativeValueError as e:
        print("Ошибка:", e)
