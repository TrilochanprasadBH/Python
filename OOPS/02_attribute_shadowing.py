class LearnAttributeShadow:
    name = 'trilochan'
    profession = 'IAS'

learn = LearnAttributeShadow()
print(learn.name)
print(learn.profession)

learn.name = 'aryaman'
print('after changing name on instantiated obj, checking on obj:-',learn.name)
print('after changing name on instantiated obj, checking on class:-',LearnAttributeShadow.name)

del learn.name
print('after deleting name from instantiated obj , checkign name on obj:-',learn.name)
#here above you can see, now name is again shown as trilchan after deleting learn.name (ie - aryaman)
#this process of instantiated obj attribute value falling back on value of that attribute in class is called attribute shadowing 
#but condition is DELETED ATTRIBUTE FROM INSTANTIATED OBJ , has to be present in class 

#if deleted attribute of instantiated obj is not present in class, then there can be no fall back , 
#look below and learn this from age example, age is added into instantiated obj , age is not present in the class 

learn.age = 29
print('age is attri added to instantiated obj learn:-',learn.age)
del learn.age 
print('after deleting learn.age , as age is only in learn, not in class, see error u get',learn.age)
#we get attribute error , as there is no fallback , and it is deleted from learn obj 

#thats it ,this is attribute shadowing
