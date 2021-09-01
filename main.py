import time
import os

class player:
  def __init__(self, pnum, word, usword, wrongcount, wrongletters, guessedletters, gameboard):
    self.pnum = pnum
    self.word = word
    self.usword = usword
    self.wrongcount = wrongcount
    self.wrongletters = wrongletters
    self.guessedletters = guessedletters
    self.gameboard = gameboard

  def usgen(self, word):
    usword = ''
    for letter in word:
      if letter in self.guessedletters:
        usword+= f" {letter} "
      else:
        usword+=" _ "
    return usword
      
def turn(player, otherplayer):

  global win

  print(f"Wrong Letters: {player.wrongletters}")
  print(f"Board:\n{player.gameboard[player.wrongcount]}")
  print(otherplayer.usword)

  playerguess = input(f"\nPlayer {player.pnum} Type in a Letter/Word: ")
  player.guessedletters.append(playerguess)

  os.system("clear")

  if playerguess == otherplayer.word: #if playerguess matches otherplayer word exactly
    otherplayer.usword = player.usgen(otherplayer.word)
    print(f"Wrong Letters: {player.wrongletters}") #Prints list of wrong letters
    print(f"Board:\n{player.gameboard[player.wrongcount]}") #Prints Stick Figure
    print(" ".join(otherplayer.word)) #Prints the word separated by spaces between each letter
    print(f"🎉 Player {player.pnum} Wins! 🎉")

    win += 1
    time.sleep(5.0)
    os.system("clear")
    
  elif playerguess in otherplayer.word: #if playerguess finds a letter in the otherplayer word
    otherplayer.usword = player.usgen(otherplayer.word)
    print(f"Wrong Letters: {player.wrongletters}")
    print(f"Board:\n{player.gameboard[player.wrongcount]}")
    print(otherplayer.usword)

    time.sleep(1.0)
    os.system("clear")

  else: #if playerguess is wrong
    player.wrongletters.append(playerguess)
    player.wrongcount += 1
    print(f"Wrong Letters: {player.wrongletters}")
    print(f"Board:\n{player.gameboard[player.wrongcount]}")
    print(otherplayer.usword)
    time.sleep(1.0)

    if player.wrongcount == 5:
      print("\n⚠️ You have one more try remaining! ⚠️")
      time.sleep(2.0)

    elif player.wrongcount == 6:
      os.system("clear")
      print(f"🎉 Player {otherplayer.pnum} Wins! 🎉")
      time.sleep(1.0)
      print(f"⭕ The correct word was {otherplayer.word}! ⭕")

      win += 1
      time.sleep(5.0)
    os.system("clear")

def intro():

  global p1,p2

  print("Player 1's Turn")
  p1word = input("Player 1 Choose a Word: ")
  p1 = player(1, p1word, " _ "*len(p1word), 0, [], [], gameboard)

  os.system("clear")
  print("Player 2's Turn")
  p2word = input("Player 2 Choose a Word: ")
  p2 = player(2, p2word, " _ "*len(p2word), 0, [], [], gameboard)
  os.system("clear")

gameboard = [" ","O","O\n|"," O\n/|"," O\n/|\\"," O\n/|\\\n/"," O\n/|\\\n/ \\"]

intro()

win = 0
while win != 1:
  turn(p1,p2)
  if win != 1:
    turn(p2,p1)