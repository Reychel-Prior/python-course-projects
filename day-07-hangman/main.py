import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(word_list)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

is_end = False
guessed_letters = []

while not is_end:

    print(hangman_art.stages[lives])
    print(f"Number of lives left: {lives}")
    guess = input("Make your guess: ").lower()

    print("You have already guessed " + guess + "!")
    display = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        elif letter == guess:
            display += letter
            guessed_letters.append(guess)
        else:
            display += "_"

    print(chosen_word)
    print(display)

    print(f"You guessed {guess}, but that letter is NOT in the word! You lose a life.")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            is_end = True
            print(hangman_art.stages[lives])
            print("* * * You lose! * * * ")
            print("The word to guess was: "+ chosen_word)

    if "_" not in display:
        is_end = True
        print("* * * You win! * * * ")