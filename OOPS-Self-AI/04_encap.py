#learning encapsulation 
#encapsulation is all about - private ,  public ,protected attributes / methods 



#access modifiers
class Example:
    def __init__(self):
        self.public = "Everyone can see this"
        self._protected = "Only class and subclasses should use this"  
        self.__private = "Only this class can access this"
    
    def show_access(self):
        print(self.public)      # ✅ Works
        print(self._protected)  # ✅ Works  
        print(self.__private)   # ✅ Works (we're inside the class)

obj = Example()
obj.show_access()
print(f"printing obj.public {obj.public}")      # ✅ Works
print(f"printing obj.protected {obj._protected}")  # ⚠️ Works but shouldn't (convention)

# Python's name mangling for private attributes
print(f"printing private using name mangling-never do this : {obj._Example__private}")  # ✅ Works but don't do this!

#trying to print private attribute
print(f"printing a private object {obj.__private}") # ❌ AttributeError
