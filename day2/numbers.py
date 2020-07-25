'''
Numbers examples
'''

num1 = 10
num2 = num3 = 20.1
num6,num7 = 20,30
num5 = '30'
print(num6+num7)
# print(num1+num5)
print(num1+int(num5))
# print("test")
print(bin(num1))

#type()
print(type(num1))
print(type(num5))
print(type(num2))

print(float(num1))
print(complex(10,2))

#isinstance()
print(isinstance(num1,int))
print(isinstance(num1,float))

#absolute
print(abs(complex(10,2)))

# int + float
print(num1+num2)

#operator Precedence
print(10*2**2)
#operator associativity
print(10*(2+(6*7))*2)

#left shift
a = 2
print(a<<2) #0010 --> 0001 0000

#right shift
a = 4
print(a>>2) #0100 --> 0001

x = range(3, 6)
for n in x:
  print(n)