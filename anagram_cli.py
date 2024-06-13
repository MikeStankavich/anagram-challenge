from anagram import Anagram


def play_anagram_game():
    print("Hello, let's play the anagram game!")
    
    difficulty = int(input("Enter the difficulty of the puzzle 1-15: "))
    unsolvable = False
    anagram = Anagram(difficulty=difficulty, unsolvable=unsolvable)
    correct_anagrams = anagram.get_puzzle_answers()
    puzzle = anagram.generate_anagram_puzzle()
    print(f"Your puzzle is: {puzzle}")
    
    user_answers = input("Enter your solutions (separated by commas): ")
    user_answers = user_answers.split(',')
    
    if not unsolvable:
        for user_answer in user_answers:
            if anagram.is_anagram(user_answer):
                print(user_answer, "is a valid solution!")
                correct_anagrams.remove(user_answer.upper())
            else:
                print(user_answer, "is not a valid solution.")
        if len(correct_anagrams) == 0:
            print("Congratulations, you solved the puzzle!")
        else:
            print("You missed the following solutions:", correct_anagrams)
    else:
         print("This puzzle is unsolvable.")


if __name__ == "__main__": 
    play_anagram_game()
