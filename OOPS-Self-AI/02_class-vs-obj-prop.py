#class attributes are available to all objects that are instantiated from that class. 
#also the class attributes can be changed by any object that is instantiated from the class 

class Learning: 
    learning_needs='focus'
    learning_needs_count=0

    def __init__(self,name,age):
        self.name=name
        self.age=age 
    
    def change_class_variable(self):
        print(f"Name:{self.name}")
        print(f"Name:{self.age}")
        Learning.learning_needs_count+=1

l1 = Learning('trilochanprasad',29)
l1.change_class_variable()
l1.change_class_variable()
l1.change_class_variable()
l1.change_class_variable()
print(Learning.learning_needs_count)