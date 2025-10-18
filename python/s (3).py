with open("input.txt", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)
letters = sum(ch.isalpha() for ch in text)
words = len(text.split())
lines_count = len(lines)

print("File contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines_count} lines")
