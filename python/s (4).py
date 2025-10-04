
list_1 = [2,3,4,5,3,4,5,2,2,5,3,4,3,5,4]
list_2 = [4,2,3,5,3,5,4,2,2,5,4,3,5,3,4]
list_3 = [5,4,3,3,4,3,3,5,5,3,3,3,3,4,4]

def fix_grades(grades):
    new_list = []          # создаём пустой список
    for i in range(len(grades)):    #проходим по индексам
        if grades[i] == 2:          #если "2", то пропускаем
            continue
        elif grades[i] == 3:        #если "3", то заменяем на "4"
            new_list.append(4)
        else:                       #иначе оставляем как есть
            new_list.append(grades[i])
    return new_list

# Применяем к каждому списку
fixed_1 = fix_grades(list_1)
fixed_2 = fix_grades(list_2)
fixed_3 = fix_grades(list_3)

print("Вариант 1:", fixed_1)
print("Вариант 2:", fixed_2)
print("Вариант 3:", fixed_3)
