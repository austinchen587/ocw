import random, string

string = "*pp*"
help = ""

word = "apple"

for i in word:
    if i not in string:
        help += i

print(help)
result = random.choice(help)

print(result)