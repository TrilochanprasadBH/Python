from functools import wraps
#build a auth decodator , any func wrapped in this, should be run only by admin 

def auth_decorator(func):
    @wraps(func)
    def wrapper(role_type):
        if role_type != 'admin':
            print('Access denied ,only admin can access this')
            return None #return is optional here, upto me,but good practise if done 
        else:
            print('Welcome Admin')
            return func(role_type) #return is optional here, upto me, but good practise if done 
    return wrapper

@auth_decorator
def give_role(type):
    print(f"this rbac role is {type}")
give_role('not_admin')
give_role('admin')
