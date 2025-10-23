class Car:
    def __init__(self, make, model): #функция инициализации 
        self.make = make #марка
        self.model = model #модель
    
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla") #создание объекта
my_car.drive()