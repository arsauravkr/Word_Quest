# Guess That Animal

A fun and engaging word-guessing game implemented in Python. The player has to guess the name of an animal by entering one letter at a time. As a bonus, one letter will be revealed at the start.

## Problem Statement

Create a Python-based word-guessing game where the player must guess the name of an animal by entering one letter at a time. The player is given a limited number of attempts to guess the word correctly. The game should be engaging and provide feedback on each guess. Additionally, one letter is revealed at the start to make the game easier.

## Logic

1. **Word Selection**:
    - Use a predefined list of animal names.
    - Randomly select a word from the list as the secret word.

2. **Game Initialization**:
    - Display an introduction message to the player.
    - Initialize the set of guessed letters and the number of attempts based on the length of the secret word.
    - Reveal a random letter in the secret word.

3. **Game Loop**:
    - Display the current progress of the word with guessed letters revealed and unguessed letters as underscores.
    - Prompt the player to enter a letter.
    - Validate the input to ensure it is a single alphabetic character that hasn't been guessed before.
    - Check if the guessed letter is in the secret word and update the game state accordingly.
    - Provide feedback to the player after each guess, indicating whether it was correct or incorrect and how many attempts are remaining.
    - Check if the player has guessed the word correctly or if they have run out of attempts.

4. **End Game**:
    - Congratulate the player if they guessed the word correctly.
    - Reveal the secret word if the player runs out of attempts.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/guess-that-animal.git
    cd guess-that-animal
    ```

2. Run the game:
    ```bash
    python guess_that_animal.py
    ```

## How to Play

- The game will prompt you to guess the name of an animal.
- One letter will be revealed at the start.
- You will enter one letter at a time.
- If the letter is in the word, it will be revealed in the correct position(s).
- If you guess all the letters correctly before running out of attempts, you win!
- If you run out of attempts before guessing the word, you lose.

## Example

```plaintext
Welcome to Guess That Animal!
Guess the word! HINT: It's the name of an animal.

As a bonus, here's a letter revealed for you: 'a'

_ a _ _ _

Enter a letter to guess: e
Good job! 'e' is in the word.
_ a _ e _

Enter a letter to guess: t
Oops! 't' is not in the word. You have 6 attempts left.

...

Congratulations! You've guessed the word correctly.
The word was 'zebra'.
