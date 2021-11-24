class Person:
    __privateName: str    
    _proctedAge: int

    def __init__(self, name, age):
        self.__privateName = name
        self._proctedAge = age

    def getName(self):
        return self.__privateName

carlos = Person('Carlos', 14)

print(carlos._proctedAge)
print(carlos.getName())
print(carlos.__privateName)

# class Juice:
    # def __init__(self, name, capacity):
        # self.name = name
        # self.capacity = capacity

    # def __str__(self):
	# return (self.name + ' ('+str(self.capacity)+'L)')
        
    # def __add__(self, other):
        # contac_name = self.name + '&' + other.name
        # total_capacity = self.capacity + other.capacity
        # return Juice(contac_name, total_capacity)


# a = Juice('Orange', 1.5)
# b = Juice('Apple', 2.0)

# result = a + b
# print(result.__str__()) #same of under 
# print(result) #same of above
