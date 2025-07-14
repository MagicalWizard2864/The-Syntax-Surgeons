import random

def choose_word(word_list):
    return random.choice(word_list)

def display_progress(guessed_word, attempts, guessed_letters):
    print("\nCurrent word: " + ' '.join(guessed_word))
    print(f"Attempts left: {attempts}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        else:
            return guess

def play_game():
    word_list = ["rizz", "ohio", "sigma", "tiktok", "skibidi"]
    word = choose_word(word_list)
    guessed_word = ['_'] * len(word)
    attempts = 10
    guessed_letters = set()

    while attempts > 0:
        display_progress(guessed_word, attempts, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Great guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

        if '_' not in guessed_word:
            print(f"\nCongratulations!! You guessed the word: {word}")
            break
    else:
        print(f"\nYou've run out of attempts! The word was: {word}")

if __name__ == "__main__":
    play_game()