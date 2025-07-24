alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']

direction = input("Type \'e\' to encrypt and \'d\' to decrypt: ").lower()
text = input("Type your message : ").lower()
shift = int(input("type the shift no. : "))

if direction == 'e':
    encrypted = ""
    for letter in text:
        if alphabet.count(letter) > 0:  # if letter in alphabet
            temp = alphabet.index(letter) + shift
            encrypted += alphabet[temp]
        else:                           # if letter not in alphabet
            encrypted += letter
    print("the encrypted text would be: ", encrypted)

elif direction == 'd':
    decrypted = ""
    for letter in text:
        if alphabet.count(letter) > 0:
            temp = alphabet.index(letter) - shift
            decrypted += alphabet[temp]
        else:
            decrypted += letter
    print("the decrypted text would be: ", decrypted)

else:
    print("please enter either e or d !")
