#IMPORTANT , learnign to store yield value in a variable , and without it ,it doesnt progess 

def chai_customer():
    print('welcome to chai store')
    order = yield
    while True:
        print(f"order is {order}")
        order = yield

chai1=chai_customer()
next(chai1)

chai1.send('masala')
chai1.send('masala1')
chai1.send('masala2')



#dry run. 
# Step	What you do	Inside the function (in order)	Printed to console	Where it pauses after this
# 1	chai1 = chai_customer()	Nothing runs yet. Just creates the generator.	—	At function start
# 2	next(chai1)	Prints "welcome to chai store"; reaches order = yield and waits.	welcome to chai store	At order = yield
# 3	chai1.send('masala')	order becomes 'masala'; enters loop; prints; hits order = yield	order is masala	At order = yield
# 4	chai1.send('masala1')	order becomes 'masala1'; prints; hits order = yield	order is masala1	At order = yield
# 5	chai1.send('masala2')	order becomes 'masala2'; prints; hits order = yield	order is masala2	At order = yield

#in my words. 
# once we instantiate fun , chai1 is obj ref only as this is generator 
#then we use next(chai1) - this 