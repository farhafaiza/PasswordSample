import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "=-)(*&^%$#@!:;[]{}?/|"
p_word = lower + upper + numbers + symbols
length = 5
password = "".join(random.sample(p_word, length))
print(password)