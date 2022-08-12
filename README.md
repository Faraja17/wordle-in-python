# Wordle in Python

Descripton: This simple game written in Python is a result of my participation in two pair programming sessions. Yesterday, I mostly observed as my partner wrote a version of the game that I did not fully grasp. However, I did come away with a few concepts that helped me to write a more effective pseudocode for myself today. My plan was to start from the beginning and write the game in Python, more at my own level. Then, I had an opportunity to pair with fellow Recurser Jing, and we took turns as driver/navigator to successfully write a game at my level that I fully understand.

At the end of our session, we discussed possible improvements, and later, I thought of additonal improvements that I would like to make. I'll document these improvements within this ReadMe and in my commits here.

Goals for improvement:
<br>&#x2611; fix guess count to start at 1 rather than at 0
<br>&#x2611; input validation
<br>&#x2611; play again option
<br>&#x2611; randomize secret word
<br>&#11036; refactor with an object-oriented approach

## Table of contents

- [Overview](#overview)
  - [The Code](#the-code)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## Overview

### The Code

```python

from random import randint


def greeting():
  print("\nWelcome to Wordle!\n\nTo win: Guess the 5-letter secret word.\n\nResults Key: B = no match, Y = match, G = match + correct spot\n__________\n")

def wordle():
  wordList = ["apple", "batch", "house", "sport", "brush", "peace", "trout", "break", "horse", "globe"]
  randomNum = randint(0, 9)
  computer_word = wordList[randomNum]
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
      # print(str(guess_count) + "/6 guesses. " + str(results))
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

```

### Links

- Live Site URL: [Play the game on Replit!](https://replit.com/@faraja/Wordle#main.py) -Click the green "Run" button and play in the console.

## My process

Jing introduced me to string interpolation. I LOVE it! so much better than having to remember to convert things into strings or integers. It reminds me of the concatenatation method for JS E6.

I am very pleased with how easily I was able to add input validation, add a play again option, and randomize the secret word. This means that I've retained what I learned working on my RPS and TTT games!

### Built with

- Python 3

### What I learned

- review of concatenation
- string interpolation

### Continued development

### Useful resources

- [String Interpolation](https://www.programiz.com/python-programming/string-interpolation) - Jing referred me here to learn about string interpolation
- []() - annotation
-

## Author

Faraja Thompson

- [My Personal Website](https://faraja17.github.io/my-website/)
- [My Blog: teach=>tech](https://teach2tech.hashnode.dev/)
- [Faraja Thompson, M.Ed. on LinkedIn](https://www.linkedin.com/in/faraja-thompson-m-ed-70885b8/)

## Acknowledgments

I'd like to acknowledge my son and mentor [DeForestt Thompson](https://github.com/DeForestt). His steadfast support and encouragement keep me motivated! Thanks for forcing me to use the command-line, Son <3 <3 <3.
