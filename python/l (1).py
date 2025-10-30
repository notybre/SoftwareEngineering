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