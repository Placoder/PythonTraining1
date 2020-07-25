
def tet(ls):
    # ls = [4,5,6]
    ls[1] = 8
    print(ls)

ls1 = [1,2,3]
ls2 =ls1
ls2 = ['b','c']
print(type(ls1))

tet(ls1)
print(ls1)
print(ls2)

a = (1,2,3)
print(id(a))

a = (3,4,5,6)
print(a)
print(id(a))

a = [1,2,3]
b = [1,2,3]
print(id(a),id(b))

a = {1,2,3}
a.add(3)
print(a)

