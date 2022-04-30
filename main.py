# first computer generation a number
import random
  
EASY_LEVEL_TATOL = 10
HARD_LEVEL_TATOL = 5
def game(): 
  print("welcome to guess number game.")
  user_number = int(input("please guess a int number from 1 - 100:"))
  
  # creat a variable to save number 
  computer_number = random.randint(1,100)
  # set difficulty
  def set_difficulty():
    level = input("Choose a level.Type'easy'or'hard'")
    if level == "easy":
      return EASY_LEVEL_TATOL
    else:
      return HARD_LEVEL_TATOL
      
  # creat a variable to memory the number of guess
  tatol = set_difficulty()
  
  # calculate the succes of fail
  def check_number(guess,answer,tatol):
    """ check the guess and tatol right or wrong"""
    if guess == answer:
      print("Bingo")
    elif guess > answer:
      print("it's large!")
      return tatol - 1
    else:
      print("it's small")
      return tatol - 1
      
  while user_number != computer_number:
    print(f"you have {tatol} attempts.remaining to guess the number.")
    user_number = int(input("again:"))
    tatol = check_number(user_number,computer_number,tatol)
    if tatol == 0:
      print("you have run out of guess.you are loser")
      return


game()
  
 