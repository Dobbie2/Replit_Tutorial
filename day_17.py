while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")
print()
print()


from getpass import getpass as input

print()
print ("EPIC 🪨  🗒️  ✂️  Battle")
print()

count = 0
score1 =( 0)
score2 = (0)
while True:
    player1 = input("Player 1 select your move( R, P ot S: ")
    player2 = input("Player 2 select your move (R, P ot S: ")
    print()
    R = ("Rock")
    P = ("Paper")
    S = ("Scissors")
    if (player1 == 'R' and player2 == 'P'):
        print ("Player1's Rock is smothered by Player2's paper!")
        score1 += 1
        count += 1
    if count == (3):
        exit()
    elif (player1 == 'P' and player2 == 'R'):
        print ("Player2's Rock is smothered by Player1's paper!")
        score2 += 1
    elif (player1 == 'S' and player2 == 'P'):
        print ("Player2's paper is cut by Player1's scissors!")
        score2 += 1
    elif (player1 == 'P' and player2 == 'S'):
        print ("Player1's paper is cut by Player2's scissors!")
        score1 += 1
print ("Game over!")