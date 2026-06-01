  🧠 Quiz Game

A terminal-based quiz game that reads questions from an external text file and tests your knowledge across 10 rounds, with a final score at the end.

   📋 About

This project separates the game logic from the question content — all questions and answers live in `question_bank.txt`, making it easy to swap in any topic you want. The game presents 10 questions, tracks your score live, and asks if you want to play again at the end.

   ⚙️ How It Works

- You enter your name and confirm you want to play
- 10 questions are read one by one from `question_bank.txt`
- Each question shows the question text and answer options
- You type your answer and get instant feedback (Correct / Incorrect)
- At the end, your final score out of 10 is displayed
- You can choose to play again or quit

   🚀 How to Run

```bash
python quiz_game.py
```

Make sure `question_bank.txt` is in the same folder.

  Sample Interaction:  
```
Welcome to the Quiz
Enter your name: Zeeshan

Do you want to start the game? Y/N: Y
Okay, Let's Play!

Quiz Game       Score: 0

Question Number 1
What is the capital of France?
A) Berlin  B) Paris  C) Rome  D) Madrid
Your Answer: B
Correct Answer! Now your score is: 1
```

   🛠️ Built With

- Python 3
- `time`, `os` modules
- File I/O (`question_bank.txt`)

   📁 File Structure

```
Quiz-Game/
├── quiz_game.py
└── question_bank.txt
```

   💡 Concepts Used

- File I/O (reading questions line by line)
- Loops and conditionals
- Score tracking
- String methods (`.upper()`, `.strip()`)
- Separation of data and logic

---
 Part of my Python beginner projects series 🐍 
