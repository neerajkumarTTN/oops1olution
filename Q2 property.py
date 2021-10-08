class Person:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        if age >=0:
            self._age=age
        else:
            self._age=0
    #setting values
    def set_age(self,new_age):
        if new_age>=0:
            self._age= new_age
        else:
            self._age=0
    #@property
    #def age(self):
        #return self._age
#p1=Person("Ram","kumar",20)
p1=Person("Ram","kumar",-20)
print(p1._age)