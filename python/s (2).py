import random

def dice():
    value = random.randint(1, 6)   # случайное число от 1 до 6
    print(f"Выпало: {value}")
    if value in (5, 6):
        print("Вы победили")
    elif value in (3, 4):
        dice()                     # рекурсивный вызов
    else:
        print("Вы проиграли")
if __name__ == "__main__":
    dice()
