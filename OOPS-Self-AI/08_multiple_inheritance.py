#multiple inheritance learning ,
#see how multiple inheritance works 

class A:
   
     def fly(self):
        print('this is fly')
    
class B(A):
    def cry(self):
        print('this is cry')

class C(A):
    def fry(self):
        print('this is fry')

class D(B,C):
    def __init__(self, name):
        self.name=name
    
    def checkPrint(self):
        print(f"this is : {self.name}")

d=D('trilochan')
d.cry()
d.fry()
d.checkPrint()