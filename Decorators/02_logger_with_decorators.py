from functools import wraps
#build a logger using decorators 

def logger_decorator(func):
    @wraps(func) #this retains the data passed
    def wrapper(*args, **kwargs):
        print(f"This is before {func.__name__} execution")
        result = func(*args,**kwargs)
        print(f"This is after {func.__name__} execution")
    return wrapper

@logger_decorator
def expert_tp(type,skills="amazing"):
    print(f"this is trilochanprasad expertise : {type} and skills are {skills}")

expert_tp('React+Agentic AI',['nextjs','front end system design'])
#output 

# This is before expert_tp execution
# this is trilochanprasad expertise : React+Agentic AI and skills are ['nextjs', 'front end system design']
# This is after expert_tp execution
