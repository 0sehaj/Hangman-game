#Hangman game
#author:Sehajleen Kaur

#make a list of names that the user has to guess randomly
x = ("dog","meow","magic","horse","dragon","cow","mouse","beans","shark")

#create a while loop to come back to the question
while True:
  y = input("Do you wanna play the Hangman Game? (yes/no) ")

#use if statements for various resposes to respective input 
  if y == "no":
    print("Okay goodbye!")
    break
  elif y == "yes":
    import random
    a = random.choice(x)
    b = len(a)
    c = "_"*b
    turn = 0

#create a while loop repeat the letter guessing till needed
    while True:
      print(c)
      d = input("Guess a letter: ")

#use if statements to process the game depending on the input
      if d in a:
        print("Great guess!")
        e = a.find(d)
        c = c[:e] + d + c[(e+1):]
    
#nest an if statement to proceed if the played has guessed the word correctly
        if c == a:
          print(c)
          print("Well done!")
      else:
        print("Try Again.")
        turn = turn + 1

#use if statements for number of turns that user has guessed the wrong word to display the parts of hangman and eventually ending the game on the last part of hangman
        if turn == 1:
          print("_________ ")
          print("  |    |")
          print("  |    O")
          print("  |")
          print("  |")
          print("  |")
        elif turn == 2:
          print("_________ ")
          print("  |    |")
          print("  |    O")
          print("  |    |")
          print("  |")
          print("  |")
        elif turn == 3:
          print("_________ ")
          print("  |    |")
          print("  |    O")
          print("  |   /|\ ")
          print("  |")
          print("  |")
        elif turn == 4:
          print("_________ ")
          print("  |    |")
          print("  |    O")
          print("  |   /|\ ")
          print("  |   / \ ")
          print("  |")
          print("GAME OVER.")
          print("YOU ARE HANGED...")

#use another if statement to respond when the user has either won or ran out of turns
      if turn == 4 or c == a:
        print("Another game maybe...")
        break

  else:
    print("Please respond in yes or no")
    continue
