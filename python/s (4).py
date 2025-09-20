s = input("Введите предложение: ")

print("Длина:", len(s))
print("В нижнем регистре:", s.lower())
print("Количество гласных:", sum(ch in "aeiou" for ch in s.lower()))
print("Замена ugly:", s.replace("ugly", "beauty"))
print("Начинается с 'The':", s.startswith("The"))
print("Заканчивается на 'end':", s.endswith("end"))