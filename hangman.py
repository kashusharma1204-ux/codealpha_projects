import random

#  predefined words
words = ["python", "programming", "india", "internship", "hired"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("===== Welcome to Hangman Game =====")
print("Guess the word one letter at a time!")

while wrong_guesses < max_attempts:

    # Display guessed letters and blanks
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check win condition
    if "_" not in display:
        print("\n Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Attempts left:", max_attempts - wrong_guesses)
        
if wrong_guesses == max_attempts:
    print("\n Game Over!")
    print("The correct word was:", word)