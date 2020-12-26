#You are free on this assignment.
#You can set the rules yourself. Ther is only one thing expected of you.
#When entering the game,The User's name and for example "Welcome John" should be pressed to the screen.
#When the game over, exit the game. So let the game end.

# Guess the Number !!! 
#Karşınızdaki kişinin tuttuğu sayıyı bulma oyunu.

import random
name = str(input("Please enter your name : "))
print("Welcome ", name)

r = random.random()

tahmin = int(100*r) + 1

alt_limit = 1
üst_limit = 100

print("benim tahminim bu", tahmin)

a = input()

while a != "doğru":
    if a == "büyüktür":
         alt_limit = int(tahmin)
         tahmin = int((üst_limit + alt_limit)/2)
         
         print(tahmin)
          
         a = input()
    elif a == "küçüktür":
         üst_limit = int(tahmin)
         tahmin = int((üst_limit + alt_limit)/2)
         print(tahmin)
        
         a = input()
         
print("doğru")    


