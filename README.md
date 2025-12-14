# Tic Tac Toe with Unbeatable AI (Minimax Algorithm)

A Python-based **Tic Tac Toe** game featuring an **unbeatable AI** powered by the **Minimax algorithm**. 
The AI evaluates all possible game states and always plays optimally, ensuring it never loses. 
The game runs in the terminal and allows a human player to compete against the AI.

## Features

* Human vs AI gameplay
* Player uses **X**, AI uses **O**
* Unbeatable AI using the **Minimax algorithm**
* Console-based interactive interface
* Input validation for user moves
* Score tracking (Wins / Losses / Draws)
* Option to replay the game

---#  Algorithm used: Minimax

The **Minimax algorithm** is a recursive decision-making algorithm used in game theory. In this project:

* The AI (O) tries to **maximize** its score
* The Human (X) tries to **minimize** the AI’s score
* All possible future game states are evaluated
* The AI always chooses the move with the best guaranteed outcome

👉 Result: **The AI never loses** (best possible outcome for human is a draw).

---

#Tech Stack

* *Language:** Python 3
* **Libraries:** Standard Python libraries only (`math`)
* **Concepts:**

  * Game Theory
  * Minimax Algorithm
  * Recursion & Backtracking
  * Object-Oriented Programming (OOP)

---

## Project Structure

```
tic-tac-toe-minimax/
│
├── tictactoe.py
├── README.md
├── .gitignore
└── LICENSE (optional)
```

---

## How to Run the Game

1 Clone the repository:

```bash
git clone https://github.com/USERNAME/REPO_NAME.git
```

2. Navigate to the project directory:

```bash
cd tic-tac-toe-minimax
```

3. Run the game:

```bash
python a.py
```

---

## GameplInstructions

* The board positions are numbered from **0 to 8**:

```
0 | 1 | 2
3 | 4 | 5
6 | 7 | 8
```

* Enter a number (0–8) to place your move
* The AI will automatically respond with the optimal move

---

## Sample Out

```
Your turn (X)Choose position (0-8): 4
AI is thinking...
AI chose position 0
```

---

##  Learning Outcomes

* Understanding  the Minimax algorithm
* Practical use of recursion and backtracking
* Experience with game logic and state evaluation
* Improved Python OOP skills

---

# Future Enhancements

* Alpha-Beta Pruning for performance optimization
* GUI version using Tkinter or Pygame
* Difficulty levels (Easy / Medium / Hard)
* Multiplayer mode

---

#💻 Author
**Ark Gupta*
3rd Year Student, IIIT nagpur



⭐ If you like this project,don’t forget to star the reposiory!
