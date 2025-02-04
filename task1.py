import random  #generating random words

# Hangman stages to play the game
hangman_pics = [
    """
       ------
       |    |
       |
       |
       |
       |
    ========
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ========
    """
]

# Creating the List of words
words = ["shinzo", "nobita", "cindrella", "shinchan", "yumiko", "barbie", "kiteretsu", "oggy"]
word = random.choice(words)  # Choosing a random word
guessed = ["_"] * len(word)  # Hidden word representation
attempts = 0  # Initial wrong attempts

print("Welcome to The Hangman Game!\n")
print("You have only six attempts to guess the correct word. So, be careful!")

while attempts < 6 and "_" in guessed:
    print(hangman_pics[attempts])  # Displaying hangman
    print("\nWord : ", " ".join(guessed))
    guess = input("Please, Guess a letter : ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts += 1
        print(f"Wrong guess! {6 - attempts} attempts left.\n")

# Final result
if "_" not in guessed:
    print("Congratulations! You won...\n") 
    print("Yippee! You guessed the word : ", word)
else:
    print(hangman_pics[6])  # Displaying full hangman
    print("Oops! You lost... \n")
    print("The word was: ", word)
    print("Game Over!")