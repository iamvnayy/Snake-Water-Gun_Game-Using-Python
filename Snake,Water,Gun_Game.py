import random
import pyttsx3
jarvis = pyttsx3.init()
jarvis.say("Hello, sir i am jarvis and this is snake,water,gun game let's play it first you enter your choice :")
jarvis.runAndWait()
def Game():
 Choices=["snake","water","gun"]
 User_choice=input("Enter your choice(snake,water,gun): ").lower()
 Computer_choice=random.choice(Choices)
 print("Computer choosen : ",Computer_choice)
 
 if(User_choice==Computer_choice):
  print("It's a draw")
  
 elif(User_choice=="snake" and Computer_choice=="water"):
  print("Congratulations, You won")
  
 elif(User_choice=="water" and Computer_choice=="gun"):
  print("Congratulations, You won")
 
 elif(User_choice=="gun" and Computer_choice=="snake"):
  print("Congratulations, You won")
  
 elif(User_choice=="snake" and Computer_choice=="gun"):
  print("Computer won")
  
 elif(User_choice=="water" and Computer_choice=="snake"):
  print("Computer won")
 
 elif(User_choice=="gun" and Computer_choice=="water"):
  print("Computer won")

Game()
