def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    with open("fib.txt", "w", encoding="utf-8") as f:
        for num in fib(200):
            f.write(str(num) + "\n")
            print(num, end=' ')
