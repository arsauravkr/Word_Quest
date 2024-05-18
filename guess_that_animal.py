import random

# List of animal names
animal_names = '''bat cat dog fox lion bear goat wolf mole seal
hare deer puma yak lynx bison boar colt fawn pony
rabbit monkey beaver donkey gibbon jaguar koala lemur
mouse otter panda sheep sloth tiger weasel zebra
camel coyote ferret impala llama bovine
elephant armadillo chimpanzee hippopotamus kangaroo orangutan
porcupine rhinoceros anteater platypus squirrel bandicoot
pangolin chipmunk walrus wombat
hedgehog bluewhale antelope'''.split()

# Randomly choose a secret word
def secret_word(difficulty):
    if difficulty == 1:
        return random.choice([word for word in animal_names if 3 <= len(word) <= 4])
    elif difficulty == 2:
        return random.choice([word for word in animal_names if 5 <= len(word) <= 6])
    elif difficulty == 3:
        return random.choice([word for word in animal_names if len(word) >= 7])
    else:
        return random.choice(animal_names)

def display_word_progress(word, guessed_letters):
    """
    Function to display the current progress of the word being guessed.
    """
    progress = [letter if letter in guessed_letters else '_' for letter in word]
    print(' '.join(progress))

def reveal_random_letter(word, guessed_letters):
    """
    Function to reveal a random letter in the secret word.
    """
    random_letter = random.choice([letter for letter in word if letter not in guessed_letters])
    guessed_letters.add(random_letter)
    print(f"As a bonus, here's a letter revealed for you: '{random_letter}'")

def calculate_score(wrong_guesses):
    """
    Function to calculate the final score.
    """
    max_score = 100
    penalty_per_wrong_guess = 10
    score = max_score - (wrong_guesses * penalty_per_wrong_guess)
    score = max(0, score)
    return score

def play_game():
    """
    Main function to play the word guessing game.
    """
    print("Welcome to Guess That Animal!")
    print("Guess the word! HINT: It's the name of an animal.\n")

    difficulty = int(input("Choose a difficulty level: 1 (easy), 2 (medium), 3 (hard): "))
    word = secret_word(difficulty)

    guessed_letters = set()
    attempts = len(word) + 2
    correct_guesses = 0
    wrong_guesses = 0

    # Reveal a random letter at the start
    reveal_random_letter(word, guessed_letters)

    while attempts > 0:
        display_word_progress(word, guessed_letters)
        guess = input("\nEnter a letter to guess: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Oops! Enter a single alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter! Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            correct_guesses += 1
        else:
            attempts -= 1
            wrong_guesses += 1
            print(f"Oops! '{guess}' is not in the word. You have {attempts} attempts left.")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word correctly.")
            print(f"The word was '{word}'.")
            break
    else:
        print("\nOut of attempts! Better luck next time.")
        print(f"The word was '{word}'.")

    score = calculate_score(wrong_guesses)
    print(f"Your final score is: {score}")

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == '__main__':
    main()