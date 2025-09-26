class Tea:
    def __init__(self,type_,size):
        self.type = type_
        #here using underscore after type is to differentiate it with the keyword type of python. avoid using keywords as args,variables etc. 
        #this is just to show how to overcome , if at some time we need to use keywords only as arg or etc. 
        self.size = size 

    def showme(self):
        print(f"this is my {self.type} and {self.size}")

my_tea= Tea('masala',100)
my_tea.showme()