import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

ln = int(input("how many letters would you like in your password? : "))
sn = int(input("how many symbols do you want in your password? : "))
nn = int(input("how many numbers do you want in your password? : "))

password = []

for _ in range(ln):
    password.append(random.choice(letters))
for _ in range(sn):
    password.append(random.choice(symbols))
for _ in range(nn):
    password.append(random.choice(numbers))

random.shuffle(password)

print(password)
