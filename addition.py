# the class for numbers data

class Numbers:

# the __init__ method is used to initialize values of that class
#   def define our function
# instance method
     def __init__(self):
          self.__sum=0
     def addNumber(self,number):
           self.__sum+=number
     def currentSum(self):
            return self.__sum

# creating an Object
# creating intance of class numbers
numbers = Numbers()

a=['3','2','1','2']

for n in a :
   for i in n.split():
    for i in n:
        numbers.addNumber(int(i))
print(numbers.currentSum())

