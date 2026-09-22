import random

# 5 words for the game
words = ["B.tech", "Student", "Ece", "Digital", "Electronic"]

word = random.choice(words)

guessed_word = ["_"] * len(word)
wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.")

while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if guessed_letters:
        print("Guessed letters:", ", ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Good guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word.")
    print("The word was:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)

print("Thanks for playing!")

