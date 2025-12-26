# class employee:
#     company="ITC"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary} ")


# class programmer(employee):
#     company="ITC Infotech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
#     def showlanguage(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")

# a=employee()
# b=programmer()

# print(a.company,b.company)

# #multiple inheritance
# class employee:
#     company="ITC"
#     name="defaultname"
#     def show(self):
#         print(f"the name is {self.name} and the company is {self.company} ")

# class coder:
#  language="python"
#  def printlanguage(self):
#      print(f"the languageusedbycoder is {self.language}")

# class programmer(employee,coder):
#     company="ITC infotech"
#     def showlanguage(self):
#         print("the name is {self.name} and he is good with {self.language}")

# a=employee()
# b=programmer()

#types of multilevel inheritance
# b.show()
# b.printlanguage()
# b.showlanguage()

# class employee():
#     a=1
# class programmer(employee):
#     b=2
# class programmer_manager(programmer):
#     c=3

# d=programmer_manager()

# print(d.b)

#super method
# class employee():
#     def __init__(self):
#         print("this is employee constructor")
#     a=1
# class programmer(employee):
#     def __init__(self):
#         print("this is programmer constructor")
#     b=2
# class programmer_manager(programmer):
#     def __init__self():
#      super().__init__()
#      print("this is programmer constructor")
#     c=3
# f=employee()
# print(f.a)
# e=programmer()
# print(e.b,e.a)
# d=programmer_manager()
# print(d.c,d.a,d.b)

#class method
# class employee:
#     a=1
#     @classmethod
#     def show(cls):
#         print(f"the class value of a is {cls.a}")
# e=employee()
# e.a=45
# e.show()

# class employee:
#     a=1
#     @classmethod
#     def show(cls):
#         print(f"the class value of a is {cls.a}")
#     @property#getter
#     def name(self):
#         return (f"{self.fname}{self.lname}")
#     @name.setter
#     def name(self,value):
#         self.fname=value.split(" ")[0]
#         self.lname=value.split(" ")[1]
# e=employee()
# e.a=45

# e.name="harry khan"
# print(e.fname,e.lname)
# e.show()

# class Number:
#     def __init__(self, n):
#         self.n = n

#     def __add__(self, num):
#         return self.n + num.n

# n = Number(1)
# m = Number(2)

# print(n + m)

