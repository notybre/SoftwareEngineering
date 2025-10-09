def remove_first_from_tuple(tpl, value):
    #сначала найдём индекс первого вхождения вручную
    found_index = -1
    i = 0
    while i < len(tpl):
        if tpl[i] == value:
            found_index = i
            break
        i += 1

    if found_index == -1:
        #не найдено возвращаем исходный кортеж
        return tpl

    #собираем новый кортеж: все элементы до found_index и после него
    new_list = []
    i = 0
    while i < len(tpl):
        if i == found_index:
            #пропускаем этот элемент (удаляем)
            i += 1
            continue
        new_list.append(tpl[i])
        i += 1

    return tuple(new_list)

if __name__ == '__main__':
    examples = [
        ((1, 2, 3), 1),
        ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
        ((2, 4, 6, 6, 4, 2), 9)
    ]

    for tpl, val in examples:
        print("Исходный кортеж:", tpl, "Удалить:", val)
        res = remove_first_from_tuple(tpl, val)
        print("Результат:", res)

