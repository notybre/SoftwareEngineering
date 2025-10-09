
def parse_numbers_to_list_and_tuple(s):

    #разделяем по запятой
    parts = s.split(',')
    
    #очищаем элементы от пробелов и преобразуем в int по одному
    lst = []
    for i in range(len(parts)):
        token = parts[i].strip()
        if token == '':
            # пропускаем пустые токены
            continue
        try:
            num = int(token)
        except ValueError:
            #если не число пропускаем (можно бросать исключение, но здесь - пропуск)
            continue
        lst.append(num)
    
    #создаём кортеж из списка
    tpl = tuple(lst)
    return lst, tpl


# Пример использования
if __name__ == '__main__':
    s = "1, 2, 3, 4, 5"
    my_list, my_tuple = parse_numbers_to_list_and_tuple(s)
    print("Исходная строка:", s)
    print("Список:", my_list)
    print("Кортеж:", my_tuple)
