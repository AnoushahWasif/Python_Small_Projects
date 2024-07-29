import random

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def word_scramble_game():
    words = ["python", "hangman", "programming", "openai", "developer"]
    word_to_guess = random.choice(words)
    scrambled_word = scramble_word(word_to_guess)

    print("Welcome to the Word Scramble Game!")
    print(f"Scrambled word: {scrambled_word}")

    attempts = 3  # Number of attempts the player has

    while attempts > 0:
        guess = input("Guess the word: ").lower()
        if guess == word_to_guess:
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, you've used all your attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    word_scramble_game()
