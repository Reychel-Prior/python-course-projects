alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    text_to_encrypt = original_text.lower()
    encrypted_text = ""
    for letter in text_to_encrypt:
        letter_index = alphabet.index(letter)
        shifted_index = (letter_index + shift_amount) % 26
        encrypted_text += alphabet[shifted_index]

    print(encrypted_text)

encrypt(text, shift)