# Dominoes

This is a simple command-line interface (CLI) implementation for playing a game of Dominoes against an automated computer opponent. The game is written in Python and uses basic data structures to simulate the classic game logic.

## How to Play

The game consists of a standard set of Domino pieces, and the distribution of these pieces is randomized at the start of the game between the player, the computer, and the stock (remaining pieces). Players take turns adding matching numbered pieces to the "snake" of dominoes on the table. The first player to place all their pieces wins, and if no further moves are possible, the game ends in a draw.

## Game Features

- Randomized piece distribution at the beginning of the game.
- Automated computer opponent making moves based on simple logic.
- Support for both regular moves and drawing from the stockpile when no moves are available.
- Check for win conditions: one of the players runs out of pieces or specific draw conditions are met.
- Simple ASCII display of the game status, including player pieces, computer pieces, and the current state of the "snake".

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/dominoes.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Game Controls

- During your turn, enter the index of the piece you want to play.
- If you cannot make a move, enter `0` to draw from the stock.
- To play a piece on the left end of the snake, enter a negative number.

## License

This project is licensed under the [MIT License](LICENSE.txt).
