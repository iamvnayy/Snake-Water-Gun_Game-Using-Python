import random
computer_output=random.randint(1,10)
user_input=0
guesses=1
while(user_input!=computer_output):
 user_input=int(input("enter a number (1-10): "))
 if (user_input>computer_output):
    print("enter a low number")
    guesses+=1
 elif(user_input<computer_output):
    print("enter a higher number")
    guesses+=1
 else:
    print(f"You guess the right number {user_input} in {guesses} attempts")