names = ["Alice", "Bob", "Charlie"];
surname = ["Smith", "Johnson", "Williams"];

surname.extend(names);
print(f"After extend: {surname}");
names.append("Diana");
print(f"After append: {names}");
names.insert(2,"Trilochan");
names.remove("Bob");
print(f"After insert and remove: {names}");
names.pop();
print(f"After pop: {names}");

surname.sort();
print(f"After sort: {surname}");
surname.reverse();
print(f"After reverse: {surname}");


numbers = [5, 2, 9, 1, 5, 6];
print(f"Original numbers: {max(numbers)}");
print(f"Original numbers: {min(numbers)}");
print(f"Original numbers: {sum(numbers)}");
print(f"Original numbers: {sorted(numbers)}");  


strong_brew = ["espresso", "dark roast", "french press"];
print(f"Strong brew coffees: {strong_brew*3}");   #this makes array of strings 3 times 

#bytearray 

names_bytearray = bytearray(b"Hello World");
names_bytesarray = names_bytearray.replace(b'Hello',b'Mellow'); 
print(f"replaced : {names_bytesarray}");