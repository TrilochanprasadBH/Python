class LearnGetterSetter:
    def __init__(self, age):
        self._age = age #underscore is nothing more than telling python that this is lil special,

    @property
    def age(self):  #this acts like getter,we get from here
        return self._age + 2
    
    @age.setter
    def age(self,age):
        if 1<= age <=5:
            self._age = age 
        else:
            raise ValueError('age must be between 1 and 5 including')

o1= LearnGetterSetter(60)
# print(o1.age())  - observe here, generally we call method like this , but as we have used @property above, 
# we need not call o1.age(), we can just call o1.age , coz of using @property
print('we are using getter',o1.age) #calling any age, any huge numbers beyond 5 also works here , we are GETTING

#setter 
o1.age= 10
print('here we are trying to set',o1.age) #this wont print, as we are raising valueerror above , nice 



    
    