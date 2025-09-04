#enumerate 
seasons = ['Spring', 'Summer', 'Fall', 'Winter']


en1 = list(enumerate(seasons))
print(f"en1: {en1}")
# output - [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

en2= list(enumerate(seasons, start=1))
print(en2)
#output - [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


# print index and item 

names = ['Alice', 'Bob', 'Charlie']
for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")   
