import random

def random_quote():
    with open("quotes.txt", encoding="utf-8") as f:
        quotes = [q.strip() for q in f if q.strip()]
    print("Случайная цитата:")
    print(random.choice(quotes))

if __name__ == "__main__":
    random_quote()
