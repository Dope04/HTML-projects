# class Student:
#   def __init__(self, name):
#     print("This is a parameterized constructor")
#     self.name = name

# student = Student("John")

# class Student:
#   def __init__(self):
#     print("This is a non-parameterized constructor")

# student = Student()
# Python program to demonstrate
# multiple inheritance

# Base class1


# class Mother:
# 	mothername = ""

# 	def mother(self):
# 		print(self.mothername)

# # Base class2


# class Father:
# 	fathername = ""

# 	def father(self):
# 		print(self.fathername)

# # Derived class


# class Son(Mother, Father):
# 	def parents(self):
# 		print("Father :", self.fathername)
# 		print("Mother :", self.mothername)


# # Driver's code
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()

# Python program to demonstrate
# multilevel inheritance

# Base class


class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class


class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

# Derived class


class Son(Father):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)


# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
