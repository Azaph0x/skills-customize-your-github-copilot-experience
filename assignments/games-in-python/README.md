
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objetivos

Build a playable Hangman (forca) game in Python that demonstrates string manipulation, control flow, and user input handling. Students will implement game logic to select a word, process guesses, and display progress until the player wins or runs out of attempts.

## 📝 Tarefas

### 🛠️ Build the Core Hangman Game

#### Description
Create a command-line Hangman game where the program randomly selects a word and the player guesses letters until they either guess the full word or exhaust a limited number of incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Prompt the player to guess single letters and validate input (ignore repeated guesses, handle non-letters).
- Show current progress using underscores for unknown letters (example: `h _ n g m a n`).
- Track and display the number of incorrect guesses remaining.
- End the game when the word is fully guessed or attempts are exhausted.
- Display a clear win or lose message and reveal the word if the player loses.

Example interaction:

```
Welcome to Hangman!
Word: _ _ _ _ _
Guesses remaining: 6
Enter a letter: a
Good guess! Word: _ a _ _ _
Guesses remaining: 6
Enter a letter: z
Incorrect. Guesses remaining: 5
```

### 🛠️ Optional Enhancements (Bonus)

#### Description
Add one or more user-experience improvements to make the game more robust or feature-rich.

#### Requirements
Choose at least one enhancement:

- Load words from an external file and handle different difficulty levels.
- Show previously guessed letters separated into correct/incorrect lists.
- Add ASCII-art Hangman stages that progress with incorrect guesses.
- Allow the player to play multiple rounds and track wins/losses.

