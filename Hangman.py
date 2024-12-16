import word_list  # Import the word list module
import ascii_hangman  # Import ASCII Hangman graphics
import logo  # Import the Hangman logo

# Initialize game variables
lives = 6

# Display the Hangman logo
logo.logo()

# Get the chosen word from the word_list module
chosen_word = word_list.get_chosen_word()

# Create a placeholder for the guessed word
word_length = len(chosen_word)
placeholder = "_" * word_length
print(f"Word to guess: {placeholder}")

# Main game logic (example for a simple loop)
game_over = False
while not game_over:
    # Display current game status
    print(f"Lives left: {lives}")
    print("Word to guess: " + " ".join(placeholder))

    # Take user input for guessing
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the word
    if guess in chosen_word:
        placeholder = "".join(
            chosen_word[i] if chosen_word[i] == guess else placeholder[i]
            for i in range(word_length)
        )
        print(f"Good guess! {guess} is in the word.")
    else:
        lives -= 1
        print(f"Wrong guess! {guess} is not in the word.")
        print(ascii_hangman.hangman_graphic(lives))  # Display Hangman graphic

    # Check win or lose conditions
    if "_" not in placeholder:
        print("Congratulations, you guessed the word!")
        game_over = True
    elif lives == 0:
        print(f"Game over! The word was: {chosen_word}")
        game_over = True
    