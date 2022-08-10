# loop through the game six times and then return a game ended message
# word variable (list): hard code a computer word or generate word randomly from a collection of five-letter words
# ask for player input to create a guess variable (list)
# results variable (list containing BBBBB)
# iterate through the letters of the guess list
    # if a letter in guess is also in word return the results list with the place of that letter as Y
        # + return n/6 tries statement
    # if a letter in guess is also in word + is in the correct spot return the results list with the place of that letter as G
    # else return the results list wit all Bs
    # count of tries +1

def wordle():
    print("\nWelcome to Wordle!\nGuess the 5-letter secret word.\n") 
  
    computer_word = 'apple'
    guess_count = 1

    while guess_count < 7:
      results = ""
      player_word = input("What is your guess?\n")
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
        # print(str(guess_count) + "/6 guesses. " + str(results))
      print(f"{guess_count} /6 guesses. Results: {results}")    
        # if win; else
      if results == "GGGGG":
        print("Congratulations, you won!")
      else:
        guess_count += 1
    print("You have run out of chances!")  

wordle()

# paired on this code in replit with Jing!
# Goals for improvement: 
    # fix guess count to start at 1 rather than at 0
    # input validation
    # play again option
    # refactor with an object-oriented approach