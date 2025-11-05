def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопусимый возраст'
        input_func(name, age)
        
    return output_func

@check
def personal_info(name, age):
    print(f"Name: {name} Age: {age}")

if __name__ == '__main__':
    personal_info('aaa', 10)
    personal_info('bbb', 20)
    personal_info('ccc', 30, 40, 50, 1)
