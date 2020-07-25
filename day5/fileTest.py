import sys
file_name = "C:\PythonTraining\test"
file = ''
try:
   file = open(file_name, "r")
   file_text = file.read()
except IOError:
   print("There was an error reading file")
   file.close()
   sys.exit()
finally:
    print("finslly")
    if file:
        file.close()
print("Here is the content of file:::\n",file_text)
