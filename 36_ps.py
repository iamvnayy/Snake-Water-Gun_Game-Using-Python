# class TwoDVector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):
#             print(f"This is a 2D Vector: {self.x}i + {self.y}j ")
# class ThreeDVector(TwoDVector):
#     def __init__(self,x,y,z):
#      super().__init__(x,y)
#      self.z=z

#     def show(self):
#             print(f"this is a 3D Vector {self.x}i+{self.y}j+{self.z}k")
# a=TwoDVector(3,4)
# a.show()
# b=ThreeDVector(5,6,7)
# b.show()

# class Animals():
#     def show(self):
#         print("This is animal class")
# class Pets(Animals):
#     def show(selr):
#         print("This is Pets class ")
# class Dogs(Pets):
#     def bark(self):
#         print("Bow Bow")

# a=Dogs()
# a.bark()

# class Employee():
#     salary=1500000
#     increment=20
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary+(self.salary*self.increment/100)
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,newsalary):
#         self.increment= ((newsalary-self.salary)/self.salary)*100
# e=Employee()
# print(e.salary)
# e.salaryAfterIncrement=1800000
# print(e.salaryAfterIncrement)
# print(e.increment)

# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def show(self):
#         print(f"{self.real} + {self.imag}i")

#     def __add__(self, other):
#         real = self.real + other.real
#         imag = self.imag + other.imag
#         return Complex(real, imag)

#     def __mul__(self, other):
#         real = (self.real * other.real) - (self.imag * other.imag)
#         imag = (self.real * other.imag) + (self.imag * other.real)
#         return Complex(real, imag)


# # Object creation
# c1 = Complex(3, 2)
# c2 = Complex(5, 4)

# c1.show()
# c2.show()

# c3 = c1 + c2
# c3.show()

# c4 = c1 * c2
# c4.show()

# class vector():
#     def __init__(self,x,y,z):
#      self.x=x
#      self.y=y
#      self.z=z

#     def __add__(self,other):
#         result=vector(self.x+other.x,self.y+other.y,self.z+other.z)
#         return result
#     def __mul__(self,other):
#        result=vector(self.x*other.x,self.y*other.y,self.z*other.z)
#        return result
#     def __str__(self):
#        return f"vector({self.x},{self.y},{self.z})"

# v1=vector(1,2,3)
# v2=vector(4,5,6)
# v3=vector(7,8,9)

# print(v1+v2)
# print(v1*v2)

# print(v1+v3)
# print(v1*v3)

# class vector:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __str__(self):
#         return f"vector({self.x}i+{self.y}j+{self.z}k)"
    
# v=vector(7,8,10)
# print(v)

# class vector:
#     def __init__(self,l):
#         self.l=l
#     def __len__(self):
#         return len(self.l)
# v1=vector([1,2,3])
# print(len(v1))

