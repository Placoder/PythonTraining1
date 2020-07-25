# File example with exception handling
import sys
file_finish = "END"
file_text = ""
file_name = input("Enter filename with complete path: ")
try:
   # open file stream
   file = open(file_name, "w")
   print("Enter '", file_finish, "' When finished")
   while file_text != file_finish:
       file_text = input("Enter text: ")
       if file_text == file_finish:
           # close the file
           file.close
           break
       file.write(file_text)
       file.write("\n")
except IOError:
   print("There was an error writing to", file_name)
   sys.exit()
finally:
    file.close()

if len(file_name) == 0:
   print("Next time please enter something")
   sys.exit()
try:
   file = open(file_name, "r")
   file_text = file.read()
except IOError:
   print("There was an error reading file")
   sys.exit()
finally:
    file.close()
print("Here is the content of file:::\n",file_text)