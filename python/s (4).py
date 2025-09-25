def average(*args):
    return sum(args) / len(args)   # сумма делится на количество элементов

if __name__ == "__main__":
    print("Среднее:", average(2, 4, 6, 8, 10))
