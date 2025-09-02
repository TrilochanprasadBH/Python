essential = {'name','truth','falsehood','belief', 'trilo'}
non_essential = {'opinion','belief','preference', 'name','prasad', 'trilo'}

all = essential | non_essential
print(f"union with{all}")

common  = essential & non_essential
print(f"intersection:{common}") # trilo , belief ,name

print(f"difference: {essential - non_essential}") # truth, falsehood 
#from essential, what is there is in non_essential, remove it, then what is left in esential, print it

#in and not in 
print(f"difference: {'name' in essential}") 
print(f"difference: {'name' not in essential}")
