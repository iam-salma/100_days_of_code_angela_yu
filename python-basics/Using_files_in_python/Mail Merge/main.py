# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as names:
    n = names.readlines()
with open("Input/Letters/starting_letter.txt") as letter:
    l = letter.read()
    for name in n:
        letter = l.replace("[name]", name.strip())
        with open(f"Output/ReadyToSend/letterTo{name.strip()}.txt", mode='w') as file:
            file.write(letter)
