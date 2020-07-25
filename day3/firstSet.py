# set of integers
my_set = {1, 2, 3}
print(my_set)
print(type(my_set))
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
# set using set function
days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
print(days)
#create empty set
my_set = set()
print(my_set)

print(type(my_set))

Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
#add to set
Days.add("Sun")
print(Days)
#remove from set
Days.discard("Sun")
print(Days)
Days.remove("Mon")
print(Days)
Days.clear()
print(Days)

