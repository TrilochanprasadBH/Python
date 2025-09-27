class A:
    lable='This is A'

class B(A):
    lable='This is B'

class C(A):
    lable='This is C'

class D(C,B):
    # lable='This is D' --if this line is written then calling D() will print 'This is D' only 
    pass #now that i have written pass, calling should print, B or C.  it will print B coz ,
    #here order matters (B,C), prints B first, then C, if its (C,B) then it prints C and then B if called

cup = D()
print(cup.lable) #this will print C
print(B.lable) #this will print B
# print(D.mro()) #mro = method resolution order
# #or
# print(D.__mro__) #both are same, just different syntax
# #or
# print(help(D)) #gives more info, like which class is inherited from which class etc

#now by callign D , print B how to do that
