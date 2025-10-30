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
