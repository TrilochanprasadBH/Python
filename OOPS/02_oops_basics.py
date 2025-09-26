class Chai:
    origin= "India"

Chai.pincode = 124345 
print(Chai.pincode)

#instantiating objects from class 

masala = Chai()
print(masala.origin)
print(masala.pincode)

masala.pincode = 000000 #i am setting pincode to in object masala instantiated from Chai, 

print('masala pincode',masala.pincode) #pin becomes 0 only in masala obj 
print('chai pincode',Chai.pincode) # see how pin has not changed in class. 

#hence, objects instantiated from class have their own address, memory etc , 
# changing attributes in these, do not change it in class , by default, but there are ways to change if needed 