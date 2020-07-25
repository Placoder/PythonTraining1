x = "global"
def foo():
    global x
    y = "local"
    x = x * 2
    print("Inside function: ",x,y)
foo()
print("Outside function: ",x)