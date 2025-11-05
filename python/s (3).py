def add_two():
    try:
        x = float(input("Введите число: "))
        print("Результат:", x + 2)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    add_two()
