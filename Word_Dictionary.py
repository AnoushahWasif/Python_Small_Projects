from PyDictionary import PyDictionary

dictionary = PyDictionary()

def get_meaning(word):
    meaning = dictionary.meaning(word)
    return meaning

def get_synonyms(word):
    synonyms = dictionary.synonym(word)
    return synonyms

def get_antonyms(word):
    antonyms = dictionary.antonym(word)
    return antonyms

def get_translation(word):
    translation = dictionary.translate(word, 'hi')
    return translation

def get_examples(word):
    examples = dictionary.example(word)
    return examples

def get_word_of_the_day():
    word_of_the_day = dictionary.word_of_the_day()
    return word_of_the_day

def main():
    print("Welcome to Word Dictionary!")
    while True:
        print("Choose an option:")
        print("1. Get meaning of a word")
        print("2. Get synonyms of a word")
        print("3. Get antonyms of a word")
        print("4. Get translation of a word")
        print("5. Get examples of a word")
        print("6. Get word of the day")
        print("7. Quit")
        choice = input("Enter your choice: ")
        print("")

        if choice == "1":
            word = input("Enter the word: ")
            meaning = get_meaning(word)
            print(meaning)
        elif choice == "2":
            word = input("Enter the word: ")
            synonyms = get_synonyms(word)
            print(synonyms)
        elif choice == "3":
            word = input("Enter the word: ")
            antonyms = get_antonyms(word)
            print(antonyms)
        elif choice == "4":
            word = input("Enter the word: ")
            translation = get_translation(word)
            print(translation)
        elif choice == "5":
            word = input("Enter the word: ")
            examples = get_examples(word)
            print(examples)
        elif choice == "6":
            word_of_the_day = get_word_of_the_day()
            print(word_of_the_day)
        elif choice == "7":
            print("Program terminated")
            break
        else:
            print("Invalid choice. Please try again.")
            print("")

        repeat = input("Would you like to check another word? (Y/N): ")
        if repeat.lower() != "y":
            print("Program terminated")
            break
        print("")

if __name__ == "__main__":
    main()
