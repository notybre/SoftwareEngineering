Отчет по Теме #9 выполнил:
- Брейер Роман Алексеевич
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + |  |
| Задание 3 | + |  |
| Задание 4 | + |  |
| Задание 5 | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

---
# Лабораторная работа 9

**ТЕМА 9. Концепции и принципы ООП**

---

## Задание 1
Допустим, что вы решили оригинально и немного странно познакомится
с человеком. Для этого у вас должен быть написан свой класс на Python,
который будет проверять угадал ваше имя человек или нет. Для этого
создайте класс, указав в свойствах только имя. Дальше создайте
функцию __init_ (), a в ней сделайте проверку на то угадал человек ваше
имя или нет. Также можете проверить что будет, если в этой функции
указав атрибут, который не указан в вашем классе, например,
попробуйте вызвать фамилию.


```python
class Roman:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Роман':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Роман"

person1 = Roman('Алексей')
person2 = Roman('Роман')
print(person1.name)
print(person2.name)

person2.surname = 'Петров'
```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_9/pic/l%20\(1\).PNG)

**Вывод:** с помощью `class` можно создать класс и инициализироват его.

---

## Задание 2
Вам дали важное задание, написать продавцу мороженого программу,
которая будет писать ДОбЗВИЛИ ли топпинг B мороженое и цену после
возможного изменения. ДЛЯ этого вам нужно написать класс, в котором
будет определяться изменили ли состав мороженого или нет. В этом
классе реализуйте метод, выводящий на печать «Мороженое с
{ТОППИНГ}» в случае наличия добавки, а иначе отобразится
следующая фраза: «Обычное мороженое». При этом программа должна
воспринимать как топпинг только атрибуты типа string. 


```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженое')

icecream = Icecream()
icecream.composition()
icecream = Icecream("шоколадом")
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_9/pic/l%20\(2\).PNG)

**Вывод:** внутри класса можно добавлять атрибуты и методы класса.

---

## Задание 3
Петя — начинающий программист и на занятиях €My сказали реализовать
икапсу...что-то. A вы хороший друг Пети и Ko всему прочему прекрасно
знаете, что икапсу...что-то — это инкапсуляция, поэтому решаете помочь
вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не
просто инкапсуляцией, а классом с сеттером, геттером и деструктором.
После написания класса BaM необходимо продемонстрировать что все
написанные вами функции работают.
Также вас необходимо объяснить Пете почему на скриншоте ниже в
консоли выводится ошибка.


```python
class MyClass:
    def __init__(self, value):
        self._value = value
    
    def set_value(self, value):
        self._value = value
    
    def get_value(self):
        return self._value
    
    def del_value(self):
        del self._value

    value = property(get_value,set_value,del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_9/pic/l%20\(3\).PNG)

**Вывод:** классы можно наследовать с помощью `class Class1(наследуемый класс)`.

---

## Задание 4
Вам — прекрасно H3BECTHO, что кошки M — собаки — являются
млекопитающими, но компьютер этого не понимает, поэтому вам нужно
написать три класса: Кошки, Собаки, Млекопитающие. И при помощи
“наследования” объяснить компьютеру что кошки и собаки — это
млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек
и собак, чтобы показать, что они чем-то отличаются друг от друга. 

```python
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"cat is {cat.className}, but they say {cat.sounds}")
```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_9/pic/l%20\(4\).PNG)

**Вывод:** инкапсуляция с помощью `_` или `__` указывает уровень доступа к атрибуту.

---

## Задание 5
На разных языках здороваются по-разному, HO суть остается
одинаковой, люди друг с другом здороваются. Давайте вместе с вами
реализуем программу с полиморфизмом, которая будет описывать всю
суть первого предложения задачи. Для этого мы можем выбрать два
языка, например, русский и английский и написать для них отдельные
классы, в которых будет в виде атрибута слово, которым здороваются на
этих языках. А также напишем функцию, которая будет выводить
информацию O TOM, как на этих языках здороваются.
Заметьте, что для решения поставленной задачи мы использовали
декоратор @staticmethod, поскольку нам He нужны обязательные
параметры-ссылки вроде self.


```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)

```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_9/pic/l%20\(5\).PNG)

**Вывод:** каждую строку можно вывести отдельно с помощью цикла.

---

# Самостоятельная работа 9

---

## Задание 1
Задание Садовник и помидоры.

```python
class Tomato:
    #Статическое свойство: стадии созревания
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зелёный', 3: 'красный'}

    def __init__(self, index):
        #_index уникальный номер томата (приватное)
        #_state стадия созревания (приватное)
        self._index = index
        self._state = 0  # первая стадия из словаря states

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f"Томат {self._index} теперь {Tomato.states[self._state]}.")

    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self):
        print("\nКуст растёт...")
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes.clear()
        print("Урожай собран")

class Gardener:
    def __init__(self, name, plant):
        #name публичное свойство (имя садовника)
        #_plant приватное свойство (объект TomatoBush)
        self.name = name
        self._plant = plant

    def work(self):
        print(f"\n{self.name} ухаживает за растением.")
        self._plant.grow_all()
        print(f"{self.name} закончил работу.")

    def harvest(self):
        print(f"\n{self.name} проверяет урожай...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"{self.name} собрал урожай.")
        else:
            print("не все томаты созрели!")

    @staticmethod
    def knowledge_base():
        print("""Справка по садоводству:
1. Томат проходит стадии: отсутствует - цветение - зелёный - красный.
2. Чтобы получить урожай, необходимо ухаживать за кустом до полного созревания.
3. После созревания все плоды можно собрат""")

if __name__ == "__main__":
    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener("Роман", bush)

    gardener.work()
    gardener.harvest() 

    gardener.work()
    gardener.harvest()  

    gardener.work()
    gardener.harvest() 

```

![Результат](https://github.com/notybre/SoftwareEngineering/blob/Tema_9/pic/s%20\(1\).PNG)

**Вывод:** Создан класс `MusicTrack` с полями для названия, исполнителя и длительности, а также методом `play()`, который выводит информацию о треке.

---

## Вывод

ООП - это фундаментальный подход к проектированию программ, основанный на моделировании реальных объектов и их взаимодействий.
Благодаря принципам инкапсуляции, наследования, полиморфизма и абстракции, код становится: более структурированным и читаемым, легче масштабируется и сопровождается, повторно используется в новых проектах, и в целом приближается к логике реального мира.
Таким образом, выполнение всех заданий помогло глубже понять и применить на практике ключевые концепции ООП в языке Python.

