#static methods are not designed to instantiate an obj from class so , this is drawback 
#class methods return cls with what i need , see below

class ThisOne:
    def __init__(self,chai,snack,day):
        self.chai=chai
        self.snack=snack
        self.day=day 
    
    @classmethod
    def from_dict(cls,order_data):
        return cls(
            order_data['chai'],
            order_data['snack'],
            order_data['day']
        )
    
    @classmethod
    def from_string(cls,order_string):
        chai,snack,day = order_string.split("-")
        return cls(chai,snack,day)

order1 = ThisOne.from_dict({'chai':'masala chai','snack':'bhakar wadi','day':'monday'})
order2 = ThisOne.from_string("elaichi-ladakiundi-sunday")

order3 = ThisOne('malnad chai' ,'patrode','shaniwar') #passing directly to class itself

#print(order1) #<__main__.ThisOne object at 0x1027e2900>
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)


class Testing:
    def __init__(self,text):
        self.text=text 
    def showme(self):
        print(f'this is {self.text}')

o1 = Testing('hello')
print(o1.__dict__) #this also works, even if classmethod is not used, but returns a dict {'text':'hello'},
#wihout dict it wont return unless o1.showme() is called 
o1.showme() #this is hello 


#static method example 

class Security:
    @staticmethod
    def is_valid_size(size):
        return size in ['small','medium','large']

print(Security.is_valid_size('small')) #True 


#Learning 

#static method : 
# does not receive first arg ie (self)
#utility func related to this class, class.method(pass param here), no need of instance 
#access to cls  - nope 
#access to self - nope

#class method: 
#receive cls class itself 
#operate on class itself , not instance, print on class.method.__dict__ 
#access to self - nope 