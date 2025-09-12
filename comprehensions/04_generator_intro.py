# generators compre are memory efficient as THEY DO NOT OCCUPY MEMORY AT ONCE , they[this object] must be consumed

# using [] in compre gives us a list, this occupies all memory needed at once 
# using ()  this in compre gives us a stream kind of obj , this is more memory efficient 

check = [1,2,3,4,5,6,7,8,9,12,14,15,14,17,28]

compre_list = sum([num for num in check if num>16]) #this is less memory eff as , list occupies it full memory needed, not stream like 
print(compre_list) 


#GENERATOR COMPREHENSION - MEMORY EFFICIENT 

check2 = [21,434,465,8,8769,23,21,2,3,4,5,5,6,6,7,8,89,1,2,3,12,3,43,4,5456]

generator_compre = (num for num in check2 if num>4000)
print(generator_compre)  #o/p - <generator object <genexpr> at 0x10426f510>
#this is a stream ,it needs to be consumed, it wont print like above list. 

generator_compre = sum(num for num in check2 if num>4000)
print(generator_compre) #o/p - 14225
