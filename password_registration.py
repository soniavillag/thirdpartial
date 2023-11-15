replit link: https://replit.com/join/obpebfnypx-soniavillanueva

"""
Objective: Generate an 8-character password.
Design an algorithm that enters a password character by character until completing 8
characters and at the end, it reports the complete password.
Extra points, if you validate the password, can only have numbers and letters.
"""

print("The password is 4 letters and then 4 numbers: ")
print("You'll have to guess the password in 3 tries per letter")

letter1 = input("Enter the first letter: (hint: the 12th letter of the alphabet ")
attempts = 3

if letter1 == "l":
  print("You're right!")
  
letter2 = input("Enter the second letter: (hint: the 15th letter of the alphabet ")
attempts = 3

if letter2 == "o":
  print("You're right!")
  
letter3 = input("Enter the third letter: (hint: the 22ndletter of the alphabet ")
attempts = 3

if letter3 == "v":
  print("You're correct!")

letter4 = input("Enter the fourth letter: (hint: the 5th letter of the alphabet ")
attempts = 3

if letter4 == "e":
  print("You're right!")
  
word = letter1 + letter2 + letter3 + letter4

if word == word:
  print("You're correct, the password is: " + word)

else:
  print("You're wrong")

digit1 = int(input("Enter the first digit: "))
attempts = 3

if digit1 == 2:
  print("You're right!")
  
digit2 = int(input("Enter the second digit: "))
attempts = 3

if digit2 == 3:
  print("You're right!")
  
digit3 = int(input("Enter the third digit: "))
attempts = 3

if digit3 == 4:
  print("You're right!")
  
digit4 = int(input("Enter the fourth digit: "))
attempts = 3

if digit4 == 5:
  print("You're right!")

digits= digit1 + digit2 + digit3 + digit4

if digits == digits:
  print("You're correct, the password is: 2345")

if word and digits == word and digits:
  print("This is the total password is love2345")
