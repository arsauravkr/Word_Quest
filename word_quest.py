import random

# List of animal names
animal_names = '''cat dog elephant giraffe lion tiger bear monkey
zebra horse cow sheep rabbit deer kangaroo koala panda fox wolf
bat whale shark dolphin octopus owl penguin'''.split()

# Randomly choose a secret word
secret_word = random.choice(animal_names)

def display_word_progress(secret_word, guessed_letters):
    """
    Function to display the current progress of the word being guessed.
    """
    progress = [letter if letter in guessed_letters else '_' for letter in secret_word]
    print(' '.join(progress))

def reveal_random_letter(secret_word, guessed_letters):
    """
    Function to reveal a random letter in the secret word.
    """
    random_letter = random.choice(secret_word)
    guessed_letters.add(random_letter)
    print(f"As a bonus, here's a letter revealed for you: '{random_letter}'")

def play_game():
    """
    Main function to play the word guessing game.
    """
    print("Welcome to Guess That Animal!")
    print("Guess the word! HINT: It's the name of an animal.\n")

    guessed_letters = set()
    attempts = len(secret_word) + 2

    # Reveal a random letter at the start
    reveal_random_letter(secret_word, guessed_letters)

    while attempts > 0:
        display_word_progress(secret_word, guessed_letters)
        guess = input("\nEnter a letter to guess: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Oops! Enter a single alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter! Try again.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word. You have {attempts} attempts left.")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You've guessed the word correctly.")
            print(f"The word was '{secret_word}'.")
            break
    else:
        print("\nOut of attempts! Better luck next time.")
        print(f"The word was '{secret_word}'.")

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == '__main__':
    main()
