list1 = ['science', 'math', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

print("list1[0]: ", list1[0])
print("list2[2:5]: ", list2[2:5])

print("Value available at index 2 :",list1[2])
list1[2] = 2019
print("New value available at index 2 : ",list1[2])
list2.append((8,9,10))
print(list2)

del list2[2]
print("After deleting updated list2 : ",list2)

print(list1[-1])
print(list2[-2])

print(list3[0:])
print(list3[0:2])
print(list3[-1:-3])
print(list3[-1:-3:-1])

print(type(list3))
print(len(list3))
print(any(list3))
print(all(list3))
list4 = ("we","","tr")
print(all(list4))
print(any(list4))

#concatination of list
print(list3 + list2)
print(list3 * 2)

#List of List / 2 dimensional list
names = [["pla",20],["pp",30],["tom",15]]
print(names[0])
print(names[0][0])
print(names[-1])
print(names[-1][1])
names.append(["mary",45])
print(names)