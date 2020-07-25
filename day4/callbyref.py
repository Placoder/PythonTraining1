def change(mylist1):
   #sallow copy for arguments
   mylist1.append([1,2,3,4])
   print("Values inside the function: ", mylist1)
   return


mylist = [10,20,30]
change(mylist)
print("Values outside the function: ", mylist)


def changeme(mylistnew):
   mylistnew = [1,2,3,4] # This would assig new reference in mylist (local copy)
   print("Values inside the function: ", mylistnew)
   return


mylistnew = [10,20,30]
changeme( mylistnew )
print("Values outside the function: ", mylistnew)