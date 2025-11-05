def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                raise ValueError("Файл пустой")
            print("Содержимое файла:\n", content)
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    read_file("не_пусто.txt")
    read_file("data_empty.txt")
