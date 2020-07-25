def greet(name,msg):
   print("Hello",name + ', ' + msg)
greet("Plaban","Good morning!")

def greet1(name, msg = "Good morning!"):
   print("Hello",name + ', ' + msg)
greet1("Neha")
greet1("Plaban","Welcome!!!")   #Indirect variable length argument call

def greet2(*names):
   # names is a tuple with arguments
   for name in names:
       print("Hello",name)
greet2("Monica","Neha","Plaban","Tom")

greet1(name = "Bruce",msg = "How do you do?") # 2 keyword arguments same order
greet1(msg = "How do you do?",name = "Bruce") # 2 keyword arguments (out of order)
greet1("Bruce",msg = "How do you do?")        # 1 positional, 1 keyword argument