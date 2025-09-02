# Tuples are immutable - cannot be changed after creation
person = ("Alice", 25, "Engineer")

# This will cause an error!
try:
    person[1] = 26  # TypeError: 'tuple' object does not support item assignment
except TypeError as e:
    print(f"Error: {e}")

# But you can create a new tuple , see how person tuple is used and unchanged 
updated_person = (person[0], 26, person[2])  # New tuple with updated age
print(f"Original: {person}")
print(f"Updated: {updated_person}")

#////MOST IMPORTANT BASICS#

names  = ('Alice', 'Bob', 'Charlie') #this is a tuple

(name1, name2, name3) = names #unpacking a tuple into variables
print(name1) #Alice
print(name2) #Bob      
print(name3) #Charlie

#SWAPPING VALUES 

a,b = 2,1 #tuple packing and unpacking
a,b=b,a #swapping values
print(a,b) #1 2


#membership test using 'in' and 'not in' 

print('Alice' in names) #True
print('Eve' in names) #False    
print('Eve' not in names) #True