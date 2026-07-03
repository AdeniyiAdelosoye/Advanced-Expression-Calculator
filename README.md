# Advanced-Expression-Calculator

Advanced-Expression-Calculator is a dynamic, rule-based mathematical evaluation system built with Python and Tkinter.

The project analyzes and parses complex, multi-layered mathematical strings using custom regular expression matching and string validation techniques to safely calculate raw algebraic inputs.

This project was created as an advanced software engineering experiment to explore how tokenization, syntax translation, and string expression engines work at a fundamental level. It was designed to demonstrate clear, human-readable input translations mapped directly into complex background math evaluations.

The purpose of the project is to demonstrate the combination of:

- Mathematical parsing concepts
- Python programming
- GUI development
- Regular expression syntax translation
- Software engineering fundamentals

## 🚀 Features

- **Interactive GUI:** Easy-to-use desktop interface built with Tkinter.
- **Implicit Multiplication Engine:** Automatically detects and formats unstated multiplication operations like matching coefficients right next to parentheses or word strings.
- **Dynamic Constant Handling:** Safely handles constant math string blocks without disrupting overlapping algebraic commands.

## 🔗 How It Works

The application scans input text for distinct mathematical indicators such as:

- implicit multiplier structures
- standard trigonometric functions
- reciprocal trigonometric functions
- inverse trigonometric functions
- fundamental mathematical constants

Each detected indicator translates directly into programmatic syntax. Based on the matched layout, structural boundaries are isolated using word-boundary flags to avoid string scrambling.

## 🛠️ Built With

- **Python** (Core parsing logic and evaluation environment)
- **Tkinter** (Graphical User Interface)
- **Regular Expressions - `re`** (Token pattern formatting and string translation)
- **Git** (Version control)
- **GitHub** (Project hosting and deployment)

## 📦 How to Run the Project

1. Make sure Python is installed on your computer.
2. Clone or download this repository.
3. Open a terminal or command prompt in the project directory.
4. Run the following command:

```bash
python NCalc.py
```
5. Type a math expression into the application window.
6. Click "Calculate" to evaluate the expression.


## 👨🏾‍💻 Author

**Adeniyi Adelsoye**

Computer Engineer | Software Engineering & Cybersecurity Enthusiast
