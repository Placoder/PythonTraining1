n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")


for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")