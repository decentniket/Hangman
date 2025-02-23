import random

def choose_word():
    # List of words with hints
    words_with_hints = {
        "python": "A popular programming language.",
        "hangman": "A word guessing game.",
        "programming": "The process of writing code.",
        "developer": "A person who creates software.",
        "challenge": "A task that tests someone's abilities.",
        "computer": "An electronic device for processing data."
    }
    word, hint = random.choice(list(words_with_hints.items()))
    return word, hint

def display_current_state(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def display_hangman(incorrect_guesses):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |   
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |   
           |   
           |
        """,
        """
           ------
           |    
           |    
           |   
           |   
           |
        """
    ]
    return stages[incorrect_guesses]

def hangman():
    word, hint = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(display_hangman(incorrect_guesses))
        print("\nCurrent word:", display_current_state(word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        
        # Offer a hint
        if len(guessed_letters) == 0:  # Provide hint only on the first guess
            use_hint = input("Would you like a hint? (yes/no): ").strip().lower()
            if use_hint in ['yes', 'y']:
                print("Hint:", hint)

        guess = input("Please guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print(display_hangman(incorrect_guesses))
        print("\nSorry, you've run out of guesses. The word was:", word)

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ['yes', 'y']:
        hangman()
    else:
        print("Thank you for playing! Goodbye!")

if __name__ == "__main__":
    hangman()
