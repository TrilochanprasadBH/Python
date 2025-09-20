#this is useful in todays AI world, to get streams of response in ai etc 
# but be careful with memory as they take lot of it 

def check_infinite_generators():
    count=1
    while True:
      #  yield count # or 
         yield f"count: {count}"
         count+=1

print_infi_gen = check_infinite_generators()
print_infi_gen2 = check_infinite_generators()
# print(next(print_infi_gen)) # count :1 so on below inc by 1 
# print(next(print_infi_gen))
# print(next(print_infi_gen))
# print(next(print_infi_gen))
# print(next(print_infi_gen))

for _ in range(2):
    #  print(check_infinite_generators())  this prints obj ref, rememer generator prints obj ref not value until next() is used
    print(next(print_infi_gen))


for _ in range(5):
        print(next(print_infi_gen2))
