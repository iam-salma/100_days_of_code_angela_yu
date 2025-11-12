import pygame
import time

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("beep.mp3")

morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    ' ': '/',
    '(': '-.--.',
    ')': '-.--.-',
    'а': '.-',
    'б': '-...',
    'в': '.--',
    'г': '--.',
    'д': '-..',
    'е': '.',
    'ж': '...-',
    'з': '--..',
    'и': '..',
    'й': '.---',
    'к': '-.-',
    'л': '.-..',
    'м': '--',
    'н': '-.',
    'о': '---',
    'п': '.--.',
    'р': '.-.',
    'с': '...',
    'т': '-',
    'у': '..-',
    'ф': '..-.',
    'х': '....',
    'ц': '-.-.',
    'ч': '---.',
    'ш': '----',
    'щ': '--.-',
    'ъ': '.--.-.',
    'ы': '-.--',
    'ь': '-..-',
    'э': '..-..',
    'ю': '..--',
    'я': '.-.-'}

#
# text = input("enter text to convert :")
# morse_code = ""
#
# for char in text:
#     morse_code += morse_code[char.upper()] + " "

user_text = input("Enter Text: ").upper()

print("Morse Code: ")
morse_code = ""
for char in user_text:
    morse_code += morse_code_dict.get(char) or char

# Make finish playing signal, now the signal is one at the end

frequency = 1000

for symbol in morse_code:
    if symbol == '.':
        sound.play(frequency, 400)
    elif symbol == '-':
        sound.play(frequency, 500)
    else:
        time.sleep(0.5)
        sound.play(frequency, 900)
        time.sleep(0.5)
    print(symbol, end='')
    time.sleep(0.5)
