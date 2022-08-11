# loop through the game six times and then return a game ended message
# word variable (list): hard code a computer word or generate word randomly from a collection of five-letter words
# ask for player input to create a guess variable (list)
# results variable (list containing BBBBB)
# iterate through the letters of the guess list
    # if a letter in guess is also in word return the results list with the place of that letter as Y
        # + return n/6 tries statement
    # if a letter in guess is also in word + is in the correct spot return the results list with the place of that letter as G
    # else return the results list with all Bs
    # count of tries +1

from random import randint


def greeting():
  print("\nWelcome to Wordle!\n\nTo win: Guess the 5-letter secret word.\n\nResults Key: B = no match, Y = match, G = match + correct spot\n__________\n")

def wordle():
  wordList = ["apple", "batch", "house", "sport", "brush"] # random word bank
  randomNum = randint(0, 5) # random number generator
  computer_word = wordList[randomNum] # selects the word from the wordList that matches the index created by the random number
  guess_count = 1

  while guess_count <= 6:
    results = ""
    player_word = input(f"Guess {guess_count}/6. What is your guess?\n")
    if len(player_word) != 5:
      print("Guess must have exactly 5 letters. Please try again.")
      continue
    for i in range(5):
      if player_word[i] == computer_word[i]:
          results += "G"
      elif player_word[i] in computer_word:
          results += "Y"
      else:
          results += "B"
    print(f"Results: {results}")    
      # if win; else
    if results == "GGGGG":
      print("Congratulations, you won!")
      playAgain()
    else:
      guess_count += 1
  print(f"You have run out of guesses! Secret word: {computer_word}")
  playAgain()  

def playAgain():
  choice = input("\nPlay again? y or n\n")
  if choice == "y":
    print("__________\n")
    wordle()
  else:
    print("\nThank you for playing!")
    exit()

greeting()
wordle()

# paired on this code in replit with Jing!
# Goals for improvement: 
    # fix guess count to start at 1 rather than at 0
    # input validation
    # play again option
    # randomize secret word
    # refactor with an object-oriented approach