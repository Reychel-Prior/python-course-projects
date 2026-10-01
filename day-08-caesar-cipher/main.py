def caesar(direction_chosen, original_text, shift_amount):
    lower_text = original_text.lower()
    caesar_text = ""
    if direction_chosen == "decode":
        shift_amount *= -1
    for letter in lower_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            shifted_index = (letter_index + shift_amount) % len(alphabet)
            caesar_text += alphabet[shifted_index]
        else:
            caesar_text += letter

    print(f"Here is your {direction_chosen}d text: {caesar_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction_chosen=direction, original_text=text, shift_amount=shift)

    choice = (input("Do you want to continue? (y/n): ")).lower()
    if choice == 'n':
        should_continue = False
