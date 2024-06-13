from fastapi import FastAPI
from anagram import Anagram

app = FastAPI()

# get("/anagram/{puzzle_key}{words}") checks if the anagram is solved
# output: solved, not solved, trick! it's unsolvable

@app.get("/")
async def root():
    return {"message": "Welcome to the anagram game!"}

@app.get("/play_anagram/{difficulty}")
def get_anagram_puzzle(difficulty: int):
    anagram = Anagram(difficulty=difficulty)
    puzzle = anagram.generate_anagram_puzzle()
    puzzle_key = anagram.puzzle_key
    return {"anagram_puzzle": puzzle, "anagram_key": puzzle_key}

@app.get("/anagram/{difficulty}-{puzzle_key}-{word}")
def check_anagram(difficulty: int, puzzle_key: str, word: str):
    anagram = Anagram(difficulty=difficulty, puzzle_key=puzzle_key)
    return {"is_anagram": anagram.is_anagram(word)}
