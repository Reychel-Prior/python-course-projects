def decrypt(original_text, shift_amount):
    text_to_decrypt = original_text.lower()
    decrypted_text = ""
    for letter in text_to_decrypt:
        letter_index = alphabet.index(letter)
        shifted_index = (letter_index - shift_amount) %  26
        decrypted_text += alphabet[shifted_index]

    print(f'Decoded result: {decrypted_text}')

def encrypt(original_text, shift_amount):
    text_to_encrypt = original_text.lower()
    encrypted_text = ""
    for letter in text_to_encrypt:
        letter_index = alphabet.index(letter)
        shifted_index = (letter_index + shift_amount) % 26
        encrypted_text += alphabet[shifted_index]

    print(f'Encoded result: {encrypted_text}')

def caesar(direction_chosen, original_text, shift_amount):
    if direction_chosen == 'encode':
        encrypt(original_text=text, shift_amount=shift)
    elif direction_chosen == 'decode':
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Please chose a valid option!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)