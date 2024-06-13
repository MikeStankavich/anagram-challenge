from collections import defaultdict 
from random import choice, shuffle
from typing import Dict, List
from math import factorial

class AnagramDictionary:
    def __init__(self):
        self.sowpods = open("./sowpods")
 
    def get_dictionary(self):
        self.dictionary = defaultdict(dict)
        for word in self.sowpods:
            word = word.strip()
            sorted_word = "".join(sorted(word))
            difficulty = len(word)
            if self.dictionary.get(difficulty) and self.dictionary.get(difficulty).get(sorted_word):
                self.dictionary[difficulty][sorted_word].append(word)
            else:
                self.dictionary[difficulty][sorted_word] = [word]
        return self.dictionary
    

class Anagram:
    def __init__(self, difficulty, unsolvable=False, anagram_dictionary=None, puzzle_key=None):
        self.anagram_dictionary = anagram_dictionary or AnagramDictionary().get_dictionary()
        self.difficulty = difficulty
        self.unsolvable = unsolvable
        # validate difficulty
        if not self.anagram_dictionary.get(self.difficulty):
            raise ValueError(f"No dictionary entries for difficulty {self.difficulty}")
        self.puzzle_key = puzzle_key or choice(list(self.anagram_dictionary.get(self.difficulty).keys()))
        self.puzzle = None
        if self.puzzle_key not in self.anagram_dictionary.get(self.difficulty).keys():
            raise ValueError(f"puzzle_key '{self.puzzle_key}' not in dictionary ")
        self.answers = self.anagram_dictionary.get(self.difficulty).get(self.puzzle_key)


    def get_puzzle_key(self) -> tuple[str, list[str]]:  
        """
        Get a puzzle of a given difficulty.
        Returns:
            str: The puzzle to be solved
        """
    
        return self.puzzle
    
    def get_puzzle_answers(self) -> tuple[str, list[str]]:  
        """
        Get the answers for a puzzle.
        Returns:
            list[str]: A list of possible solutions (strings).
        """
        return self.answers
    
    def generate_anagram_puzzle(self) -> str:
        """
        Generate a puzzle by shuffling the letters of a word.
        Returns:
            str: A shuffled version of the puzzle word.
        """
        self.puzzle = list(self.puzzle_key)
        shuffle(self.puzzle)
        self.puzzle = "".join(self.puzzle)
        # Handle cases where the shuffle is one of the solutions
        if self.puzzle in self.anagram_dictionary.get(self.difficulty).get(self.puzzle_key):
            return self.generate_anagram_puzzle()
        return self.puzzle

    def generate_unsolvable_puzzle(self) -> str:
        """
        Generate an unsolvable puzzle that looks like a solvable one.
        Returns:
            str: An unsolvable puzzle that looks like a solvable one.
        """
        # Shuffle the puzzle key
        puzzle = list(self.puzzle_key)
        shuffle(puzzle)
        puzzle = puzzle[1:] + [choice(puzzle)]
        sorted_puzzle = "".join(sorted(puzzle))
        if sorted_puzzle in list(self.anagram_dictionary.get(self.difficulty).keys()):
            return self.generate_unsolvable_puzzle()
        self.puzzle = "".join(puzzle)
        return self.puzzle

    def is_anagram(self, word_to_check: str) -> bool:
        """
        Verify that the answer provided for a puzzle is correct.
        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return word_to_check in self.answers
