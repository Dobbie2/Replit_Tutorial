from getpass import getpass as input
print()
print ("EPIC 🪨  🗒️  ✂️  Battle")
print()

player1 = input("Player 1 select your move( R, P ot S: ")
player2 = input("Player 2 select your move (R, P ot S: ")
print()
R = ("Rock")
P = ("Paper")
S = ("Scissors")
if (player1 == 'R' and player2 == 'P'):
  print ("Player1's Rock is smothered by Player2's paper!")
elif (player1 == 'P' and player2 == 'R'):
  print ("Player2's Rock is smothered by Player1's paper!")
elif (player1 == 'S' and player2 == 'P'):
  print ("Player2's paper is cut by Player1's scissors!")
elif (player1 == 'P' and player2 == 'S'):
  print ("Player1's paper is cut by Player2's scissors!")
