# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
easy_pass = list()
hard_pass = list()
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

i = 1
while i <= nr_letters:
    easy_pass.append(random.choice(letters))
    i = i + 1
i = 1
while i <= nr_numbers:
    easy_pass.append(random.choice(numbers))
    i = i + 1
i = 1
while i <= nr_symbols:
    easy_pass.append(random.choice(symbols))
    i = i + 1

print(easy_pass)
i = 1
while i <= (nr_symbols + nr_numbers + nr_letters):
    ele = random.choice(easy_pass)
    hard_pass.append(ele)
    easy_pass.remove(ele)
    i += 1

print(hard_pass)
hard_pass_str = str()
for i in hard_pass:
    hard_pass_str=hard_pass_str+i
print("Your password is:", hard_pass_str)
