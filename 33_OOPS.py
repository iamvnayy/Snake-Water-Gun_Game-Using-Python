# class employee:
#     language="py" #this is class attribute
#     salary=1200000

# harry=employee()
# print(harry.language,harry.salary)

# rohan=employee()
# rohan.name="rohan" #this is object/instance attribute
# print(rohan.name,rohan.language,rohan.salary)

# class employee:
#     language="py"
#     salary=1200000

# harry=employee()
# harry.name="harry"
# print(harry.name,harry.salary,harry.language)

# rohan=employee()
# print(rohan.salary,rohan.language)

# vinay=employee()
# vinay.salary=1500000 #instance attribute always takes place of class attribute
# print(vinay.salary)

# class employee:
#     language="py"
#     salary=1200000
#     def getinfo(self):#self argument need to be pass
#        print(f"the language is {self.language} and the salary is {self.salary}")
#     #for no argument pass we need to define it as a static method

#     @staticmethod
#     def greet():
#         print("good morning")
# harry=employee()
# harry.getinfo()
# harry.greet()

# class employee:
#     language="py"
#     salary=1200000

#     def __init__(self,name,salary,language):#dunder method
#         self.name=name
#         self.salary=salary
#         self.language=language
#         print("i am creating an object")
#     def getinfo(self):
#        print(f"the language is {self.language} and the salary is {self.salary}")
#     @staticmethod
#     def greet():
#         print("good morning")
# harry=employee("harry","javascript",1600000)
# print(harry.name,harry.salary,harry.language)
# harry.getinfo()
# harry.greet()
