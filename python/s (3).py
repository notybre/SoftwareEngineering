x = int(input("Введите число 0-10: "))

if 0 <= x <= 10:
    if x <= 3:
        print("0–3")
    elif x <= 6:
        print("3–6")
    else:
        print("6–10")
else:
    print("число вне диапазона")