import random
import sys

class WordGuessGame:
    COLORS = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }

    def __init__(self, word_list, max_attempts=10):
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.stats = {"wins": 0, "losses": 0}

    def color_text(self, text, color):
        return f"{self.COLORS.get(color, '')}{text}{self.COLORS['reset']}"

    def choose_word(self):
        return random.choice(self.word_list)

    def display_progress(self, guessed_word, attempts, guessed_letters, word):
        print(self.color_text("\nCurrent word: " + ' '.join(guessed_word), "cyan"))
        print(f"Attempts left: {self.color_text(attempts, 'yellow')}")
        print(f"Guessed letters: {self.color_text(', '.join(sorted(guessed_letters)), 'yellow')}")
        unrevealed = [c for c, g in zip(word, guessed_word) if g == '_']
        if unrevealed:
            hint = random.choice(unrevealed)
            print(f"Hint: The word has {len(word)} letters. One of them is '{self.color_text(hint, 'green')}'.")

    def get_guess(self, guessed_letters):
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print(self.color_text("Please enter a single alphabetic character.", "red"))
            elif guess in guessed_letters:
                print(self.color_text("You already guessed that letter. Try another one.", "yellow"))
            else:
                return guess

    def play_round(self):
        word = self.choose_word()
        guessed_word = ['_'] * len(word)
        attempts = self.max_attempts
        guessed_letters = set()

        while attempts > 0:
            self.display_progress(guessed_word, attempts, guessed_letters, word)
            guess = self.get_guess(guessed_letters)
            guessed_letters.add(guess)

            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
                print(self.color_text("Great guess!", "green"))
            else:
                attempts -= 1
                print(self.color_text("Wrong guess!", "red"))

            if '_' not in guessed_word:
                print(self.color_text(f"\nCongratulations!! You guessed the word: {word}", "green"))
                self.stats["wins"] += 1
                return

        print(self.color_text(f"\nYou've run out of attempts! The word was: {word}", "red"))
        self.stats["losses"] += 1

    def show_stats(self):
        print(self.color_text(f"\nGames played: {self.stats['wins'] + self.stats['losses']}", "cyan"))
        print(self.color_text(f"Wins: {self.stats['wins']}", "green"))
        print(self.color_text(f"Losses: {self.stats['losses']}", "red"))

    def play(self):
        print(self.color_text("Welcome to the Advanced Word Guessing Game!", "cyan"))
        while True:
            self.play_round()
            self.show_stats()
            again = input(self.color_text("\nPlay again? (y/n): ", "yellow")).strip().lower()
            if again != 'y':
                print(self.color_text("Thanks for playing!", "cyan"))
                break

if __name__ == "__main__":
    word_list = ["rizz", "ohio", "sigma", "tiktok", "skibidi"]
    game = WordGuessGame(word_list)
    try:
        game.play()
    except KeyboardInterrupt:
        print("\n" + game.color_text("Game interrupted. Goodbye!", "red"))
        sys.exit(0)
        