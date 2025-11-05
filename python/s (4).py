class LogCall:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Вызов функции '{self.func.__name__}' с аргументами {args} {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"Функция '{self.func.__name__}' вернула: {result}\n")
        return result

@LogCall
def multiply(a, b):
    return a * b

@LogCall
def greet(name):
    return f"Привет, {name}!"

if __name__ == '__main__':
    multiply(3, 5)
    greet("Роман")
