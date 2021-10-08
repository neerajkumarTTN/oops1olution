
class Base:
	def __init__(self):
		self.a = "Hello"
		self.__c = "Neeraj"

class Derived(Base):
	def __init__(self):

		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)

obj1 = Base()
obj2=Base()
print(obj1.a)
print(obj2._c)
