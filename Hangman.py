import random

def choose_word():
    words = ["python", "hangman", "programming", "openai", "developer"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
          ---
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / 
          ---
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |    
          ---
        """,
        """
           ------
           |    |
           |    O
           |   \\|
           |    |
           |    
          ---
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    |
           |    
          ---
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |    
          ---
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |    
          ---
        """
    ]
    return stages[tries]

def play_game():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("Word: " + " ".join(["_" if letter not in guessed_letters else letter for letter in word]))
    
    while tries > 0 and word_letters:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print("Wrong guess. Try again.")

        print(display_hangman(tries))
        print("Word: " + " ".join(["_" if letter not in guessed_letters else letter for letter in word]))
    
    if not word_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_game()
