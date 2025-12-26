# a1=int(input("enter a number :"))
# a2=int(input("enter a number :"))
# a3=int(input("enter a number :"))
# a4=int(input("enter a number: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("a1 is greater")
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("a2 is greater")
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("a3 is greater")
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("a4 is greater")
    
# english=int(input("enter english marks: "))
# hindi=int(input("enter hindi marks: "))
# maths=int(input("enter maths marks: "))
# total_marks=(english+hindi+maths)/300*100

# if(total_marks>=40 and english>=33 and hindi>=33 and maths>=33):
#     print("pass")
# else:
#     print("fail")

# comment=input("enter a comment : ")
# if(comment=="make a lot of money" or comment=="buy now" or comment=="subscribe this" or comment=="click this"):
#     print("it is a spam email")
# else:
#     print("mail is not spam")

# username=input("enter the username: ")
# if(len(username)<10):
#     print("username character length is less then 10")
# else:
#     print("username length is greater then 10")

# l=("Harry","Vinay","Rohan")
# name=input("enter name :")
# if(name in names):
#     print("Name is present")
# else:
#     print("name is not present")

# marks=int(input("enter marks of the student: "))
# if(marks<=100 and marks<=90):
#     grade="ex"
# if(marks<=90 and marks<=80):
#     grade="A"
# if(marks<=80 and marks<=70):
#     grade="B"
# if(marks<=70 and marks<=60):
#     grade="C"
# if(marks<=60 and marks<=50):
#     grade="D"
# if(marks<50):
#     grade="F"
# print("grade is : ",grade)

comment=input("enter a comment :")
if("harry" in comment.lower()):
    print("post is talking about harry")
else:
    print("post is not talking about harry")
