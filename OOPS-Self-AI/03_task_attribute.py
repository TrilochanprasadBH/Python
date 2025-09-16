#create a class where students register their name, class, and then check eligibility to access course content, which is unique to each of them 

class Student:
    def __init__(self,name,batch):
        self.name=name
        self.batch=batch
        self.courses=[] #observe how this is not part of params , i add it here  
    
    def add_course(self, course):
        self.courses.append(course)
        print(self.courses)
    
    def check_eligibility(self):
       print('allowed' if self.batch > 10 else 'not allowed')

s1= Student('trilo',5)
s1.add_course('psir')

s1.check_eligibility()

s1= Student('trilo',15)
s1.add_course('psir')
s1.check_eligibility()