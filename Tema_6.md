Отчет по Теме #6 выполнил:
- Брейер Роман Алексеевич
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |


знак "+" - задание выполнено; знак "-" - задание не выполнено;

---
# Лабораторная работа 6

**ТЕМА 6. Базовые коллекции: словари, кортежи **

---

---

## Задание 1
В школе, где вы учились, узнали, что вы крутой программист и
попросили написать программу для учителей, которая будет при вводе
кабинета писать для него ключ доступа и статус, занят кабинет или нет.
При написании программы необходимо использовать словарь (dict),
который на вход получает номер кабинета, а выводит необходимую
информацию. Если кабинета, который вы ввели нет B словаре, то B
консоль B виде значения ключа нужно вывести “№опе” и виде статуса
вывести “False”. 


```python
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)
```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/l%20\(1\).PNG)

**Вывод:** с помощью словарей удобно обращаться к элементу по ключу. С помощью такой конструкции мы заменяем конструкцию `if/elif/else`.

---

## Задание 2
Алексей решил создать самый большой словарь B мире. Для этого он
придумал функцию dict maker (**kwargs), которая принимает
неограниченное количество параметров «ключ: значение» и обновляет
созданный UM словарь my_dict, состоящий всего U3 одного элемента
«firsty со значением «50 easy». Помогите Алексею создать данную
функцию. 


```python
from pprint import pprint
my_dict = {'first':'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4= 13)
dict_maker(name='Роман', age=19, weight=55, eyes_color='brown')
pprint(my_dict)
```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/l%20\(2\).PNG)

**Вывод:** с помощью функций и `**kwargs` можно динамически создавать словари. `pprint` позволяет удобно вывести инормацию.

---

## Задание 3
Для решения некоторых задач бывает необходимо разложить строку на
отдельные символы. Мы знаем что это можно сделать при помощи
split(), у которого более гибкая настройка для разделения для этого, но
если нам нужно посимвольно разделить строку без всяких условий, то
для этого мы можем использовать кортежи (tuple). Для этого напишем
любую строку, которую будем делить и “обвернем” ее B tuple и дальше
мы можем как нам угодно с ней работать, например, сделать ее
списком (тогда получится полный аналог split()) или же работать ¢ ним
дальше, как с кортежем.


```python
input_string = 'HelloWorld'
result=tuple(input_string)
print(result)
print(list(result))
```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/l%20\(3\).PNG)

**Вывод:** с помощью `tuple` можно посимвольно разделить строку без всяких условий.

---

## Задание 4
Вовочка решил написать крутую функцию, которая будет писать имя,
возраст и место работы, HO при этом на вход этой функции будет
поступать кортеж. Помогите Вовочке написать эту программу. 


```python
def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Георгий", 41, "Yandex")
personal_info(*bob)
```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/l%20\(4\).PNG)

**Вывод:** на вход функции в качестве аргументов можно выставить кортеж.

---

## Задание 5
Для сопровождения первых лиц государства X нужен кортеж, но никто
не может определиться с порядком машин, поэтому вам нужно
написать функцию, которая будет сортировать кортеж, состоящий из
целых чисел по возрастанию, и возвращает его. Если хотя бы одиНн
элемент не является целым числом, TO фуНКЦИЯ возвращает ИСХОДНЬ[Й
кортеж.


```python
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5,5,3,1,9)))
    print(tuple_sort((5,5,2.1,'1',9)))
```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/l%20\(5\).PNG)

**Вывод:** кортеж можно также сортировать и проверять каждый элемент в нём.

---

# Самостоятельная работа

---

## Задание 1

принять от пользователя последовательность чисел, разделённых запятыми, затем вернуть эти данные в виде списка и кортежа.

```python

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

```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/s%20\(1\).PNG)

**Вывод: **Простая и надёжная функция — вручную разбивает строку, приводит к целым и возвращает список и кортеж. Устойчиво к пробелам и пустым токенам.

---

## Задание 2

написать функцию, которая удаляет первое появление заданного значения из кортежа и возвращает новый кортеж. Если такого элемента нет — вернуть исходный кортеж (без изменений).

```def remove_first_from_tuple(tpl, value):
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


# Примеры (взяты из условия документа)
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
        print("---")
```
![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/s%20\(2\).PNG)
---
**Вывод: **Функция корректно удаляет первое найденное вхождение (при этом кортежы остаются неизменяемыми - мы создаём новый). Если элемент отсутствует, возвращаем исходный кортеж.

---

## Задание 3

дана строка, содержащая символы '0'..'9' (длина ≥ 15). Нужно создать словарь, где ключ — цифра (тип int), значение — количество её вхождений в строке. Затем *из этого словаря* функция должна вернуть словарь из 3-х самых часто встречающихся чисел (ключи — int, значения — количества). Результат вывести в порядке возрастания ключа.


```
def build_counts_dict(s):
    counts = {}  #словарь для подсчёта
    #Проходпо всем символам строки
    i = 0
    while i < len(s):
        ch = s[i]
        #учитываем только цифры
        if '0' <= ch <= '9':
            #преобразуем в int-ключ
            key = ord(ch) - ord('0')
            if key in counts:
                counts[key] = counts[key] + 1
            else:
                counts[key] = 1
        #иначе игнорируем символы (например, пробелы, запятые)
        i += 1
    return counts


def top_3_most_frequent(s):
    counts = build_counts_dict(s)
    if not counts:
        return {}

    #список пар (digit, count)
    pairs = []
    for k in counts:
        pairs.append((k, counts[k]))

    top_pairs = []
    temp_pairs = list(pairs)  # копируем
    take = 3
    while take > 0 and temp_pairs:
        #найти индекс пары с максимальной частотой (если есть tie — выбрать ту с меньшим ключом)
        max_idx = 0
        j = 1
        while j < len(temp_pairs):
            # сравним частоты
            if temp_pairs[j][1] > temp_pairs[max_idx][1]:
                max_idx = j
            elif temp_pairs[j][1] == temp_pairs[max_idx][1]:
                #при равной частоте возьмём пару с меньшим ключом (чтобы результат детерминирован)
                if temp_pairs[j][0] < temp_pairs[max_idx][0]:
                    max_idx = j
            j += 1
        #добавляем найденную пару в top
        top_pairs.append(temp_pairs[max_idx])
        # удаляем её из временного списка
        temp_pairs.pop(max_idx)
        take -= 1

    i = 0
    while i < len(top_pairs):
        min_idx = i
        j = i + 1
        while j < len(top_pairs):
            if top_pairs[j][0] < top_pairs[min_idx][0]:
                min_idx = j
            j += 1
        # обмен
        if min_idx != i:
            tmp = top_pairs[i]
            top_pairs[i] = top_pairs[min_idx]
            top_pairs[min_idx] = tmp
        i += 1

    # формируем итоговый словарь
    result = {}
    i = 0
    while i < len(top_pairs):
        k, cnt = top_pairs[i]
        result[k] = cnt
        i += 1

    return result


#пример использования
if __name__ == '__main__':
    s = "012345678901234567890123456789012345"  
    s2 = "1112233344555599999000000123456789012345"
    counts_all = build_counts_dict(s2)
    top3 = top_3_most_frequent(s2)
    print("Полный словарь частот:", counts_all)
    print("Топ-3 самых частых (словарь):", top3)
```
![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/s%20\(3\).PNG)
---

**Выводы:**
* Для выбора трёх самых частых элементов реализован алгоритм выбрать максимум 3 раза
* Итоговый словарь возвращает ровно 3 пары {digit: count} (если в исходном тексте меньше трёх разных цифр - возвращает столько, сколько есть), и при выводе ключи упорядочены по возрастанию.

---

## Задание 4

Условие: Написать функцию, которая принимает кортеж и случайный элемент (значение) x. Нужно вернуть новый кортеж, начинающийся с первого появления x и заканчивающийся вторым появлением x (включительно).

```
from typing import Tuple, Any

def slice_first_to_second(tpl: Tuple[Any, ...], x: Any) -> Tuple[Any, ...]:
    try:
        first = tpl.index(x)
    except ValueError:
        return ()
    #поиск второго - начинаем с first+1
    try:
        second = tpl.index(x, first+1)
    except ValueError:
        return tpl[first:]
    return tpl[first:second+1]

if __name__ == '__main__':
    print(slice_first_to_second((1,2,3), 8))          
    print(slice_first_to_second((1,8,3,4,8,9,2), 8))      
    print(slice_first_to_second((1,2,8,5,1,2,9), 8))        
```
![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/s%20\(4\).PNG)
**Вывод: **Функция корректно обрабатывает все три случая (0, 1 и ≥2 вхождений)

---

## Задание 5

Дан список целых чисел. Нужно вернуть кортеж из тех элементов, которые встречаются ровно два раза в исходном списке. Порядок элементов в результате - в порядке первого появления каждого такого числа в исходном списке. Если таких элементов нет - вернуть пустой кортеж.

```
from collections import Counter
from typing import List,Tuple

def elements_with_count_two(lst: List[int]) -> Tuple[int, ...]:
    counts=Counter(lst)
    seen=set()
    result=[]
    for x in lst:
        if counts[x]==2 and x not in seen:
            result.append(x)
            seen.add(x)
    return tuple(result)

if __name__=='__main__':
    print(elements_with_count_two([1,2,3,2,4,1,5])) 
    print(elements_with_count_two([7,7,7,7]))      
    print(elements_with_count_two([9,8,9,8,7,7]))  
```
![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_6/pic/s%20\(5\).PNG)
**Вывод: ** Задача проверяет логику подсчёта и сохранения порядка первого появления. 

---
# Общий вывод

Коллекции данных (списки, кортежи, множества, словари) - основа хранения и обработки информации в Python.
* Списки (list) - изменяемые упорядоченные коллекции, удобные для добавления и удаления элементов.
* Корежи (tuple) - неизменяемые последовательности, часто применяются для хранения фиксированных данных.
* Множества (set) - неупорядоченные коллекции уникальных элементов, полезные при фильтрации повторов.
* Словари (dict) - хранят пары ключ - значение и обеспечивают быстрый доступ к данным по ключу.

Использование встроенных структур данных, таких как Counter, set, а также понимание принципов итерации и индексации позволяют создавать эффективные алгоритмы для анализа и обработки информации.





