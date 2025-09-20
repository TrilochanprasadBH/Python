#normal function

def get_from_list():
    return ['one', 'two','three','four','five','six']

getting = get_from_list()
print(getting)

def get_from_generators():
    yield 'one'
    yield 'two'
    yield 'three'

get_gen = get_from_generators()
print(get_gen) # this prints this ->  <generator object get_from_generators at 0x10051e4b0>
#this only points to the object , and not print values , to print values use next()

print(next(get_gen)) #one 
print(next(get_gen)) #two
print(next(get_gen)) #three 

#hence, generators help us to: 
# 1. save memory , or get response as and when needed, i might not need results immediately
# 2. lazy evaluation 