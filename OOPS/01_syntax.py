class Chai:
    pass 

print(type(Chai)) #<class 'type'> , this means , this is class type. 

ginger_chai = Chai()
print(ginger_chai) #<__main__.Chai object at 0x10297e900> , main means this is obj, Chai shows this is obj of class Chai, and its address 

print(type(ginger_chai) is Chai) #True , as ginger_chai is instantiated from Chai class 
