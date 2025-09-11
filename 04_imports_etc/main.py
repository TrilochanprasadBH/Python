# learning ways to import in python 

# one 

import recipes.flavours

print(recipes.flavours.butterscotch()) 


#two 

from recipes import flavours

print(flavours.butterscotch())
 
#three 

from recipes.flavours import butterscotch , vanilla #press control +space after import to get suggestions 
print(butterscotch())
print(vanilla())

#four 

from recipes.flavours import * 

print("import all:",vanilla())
