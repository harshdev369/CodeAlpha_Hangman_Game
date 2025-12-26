import random

# Step 1: Word list
words = ["python","java","banana","apple","computer"]

# Step 2: Choose random word
word = random.choice(words)
guessed_letters = []
attempts = 4

print(" Welcome to Hangman Game!")
print("_ " * len(word))

# Step 3: Game loop
while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct Guess!")
    else:
        attempts -= 1
        print(" Wrong Guess! Remaining attempts:", attempts)

    # Step 4: Show word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    # Step 5: Win condition
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", word)
        break

# Step 6: Lose condition
if attempts == 0:
    print("\n Game Over! The word was:", word)
