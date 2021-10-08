class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def __repr__(self):
        return self.email
obj1=User("amit","amit.dubey@tothenew")
obj2=User("neeraj","neeraj.kumar@gmail.com")
obj3=User("abc","abc5344@gmail.com")
obj4=User("xyz","xyz123@gmail.com")
print(obj1)
print(obj2)
print(obj3)
print(obj4)