# Anagram

Your customer is a psychological research lab who is studying the phenomenon of
“perfectionism.”

The researchers in this lab decide that they will use puzzles to conduct an
experiment on self-reported “perfectionists”, determining whether those who
call themselves perfectionists react differently to difficult (or unsolvable)
puzzles than those who do not.

Through some brainstorming with the team, you come up with the idea for
generating “anagram puzzles”. These are puzzles based on re-arranging character
sequences into a valid English word.

An "anagram puzzle" is a string of scrambled letters that's not an English word
A solution to the puzzle is an English word that's an anagram of the puzzle.
Example: the puzzle “dgo” has the solutions “dog” and “god”

### Requirements

1. Generate puzzles of varying difficulty
2. Verify that the answers provided for a puzzle are correct
3. Generate unsolvable puzzles that look like solvable ones

### Usage

To use the anagram solver, follow these steps:

1. Install the required dependencies by running the command `pip install -r
   requirements.txt`.
2. Run the command `python anagram_cli.py` to execute the anagram solver in
   your terminal.
3. Run the API with `python -m uvicorn anagram_api:app --reload` to play the
   game in your browser.
4. Have fun!

### Running Tests

To run the tests for the anagram solver, follow these steps:

1. Ensure that you have installed the required dependencies by running the
   command `pip install -r requirements.txt`.
2. Open the terminal and navigate to the project directory.
3. Run the command `pytest` to execute the test suite.
4. The test results will be displayed in the terminal, indicating whether the
   tests passed or failed.

### API Endpoints

- Start game: `GET http://localhost:8000/play_anagram/5`
- Check an answer: `GET http://localhost:8000/anagram/5-DEGKY-KEDGY`

## Assignment

- The program provided has a few bugs in it. Read through the requirements and
usage listed above and see if you can identify them and fix them. There are two
bugs (that we know of).
- Dockerize the Anagram App.
