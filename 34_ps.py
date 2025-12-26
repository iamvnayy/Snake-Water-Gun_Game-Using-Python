# class Programmer:
#     def __init__(self,name,salary,role):
#         self.name=name
#         self.salary=salary
#         self.role=role
# Harry=Programmer("Harry",1500000,"Software engineer")
# print(Harry.name,Harry.salary,Harry.role)
# Rohan=Programmer("Rohan",1600000,"Python engineer")
# print(Rohan.name,Rohan.salary,Rohan.role)
# Vinay=Programmer("Vinay",1700000,"Software engineer")
# print(Vinay.name,Vinay.salary,Vinay.role)

# class calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         return self.n*self.n
#     def squareroot(self):
#         return self.n**0.5 
#     def cube(self):
#         return self.n*self.n*self.n
# n=int(input("enter a number : "))
# calc=calculator(n)
# print(f"the square of {n} is {calc.square()}")
# print(f"the cube of {n} is : {calc.cube()}")
# print(f"the squareroot of {n} is : {calc.squareroot()}")

# class a:
#     a=0.5

# object=a()
# object.a=0
# print(object.a)

# class calculator:
#     def __init__(self,n):
#         self.n=n
#     @staticmethod
#     def greet():
#         print("Hello")
#     def square(self):
#         return self.n * self.n
#     def squareroot(self):
#         return self.n **0.5
#     def cube(self):
#         return self.n*self.n*self.n

# n=int(input("enter a number : "))
# calc=calculator(n)
# print(f"the sqaure of {n} is : {calc.square()}")
# print(f"the sqaureroot of {n} is : {calc.squareroot()}")
# print(f"the cube of {n} is : {calc.cube()}")



# class employee():
#     def greet(slf):
#         return "harry"
    
# object=employee()
# print(object.greet())         

# class Train:
#     def __init__(self,name,seats,fare):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
#     def get_fare(self):
#         print(f"the fare of train is :{self.fare}")
#     def get_status(self):
#         print(f"the number of seats available :{self.seats}")
#     def book_ticket(self):
#         if(self.seats>0):
#             print("your seat booked succesfully")
#             self.seats-=1
#         else:
#             print("seat not available")

# reserve=Train("Rajdhani express",5,1500)
# reserve.get_fare()
# reserve.get_status()
# reserve.book_ticket()