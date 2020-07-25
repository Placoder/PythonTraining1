import sys
file_finish = "END"
file_text = ""
file_name = input("Enter filename with complete path: ")

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
file.close()

if len(file_name) == 0:
   print("Next time please enter something")
   sys.exit()

file = open(file_name, "r")
file_text = file.read()
file.close()
print("Here is the content of file:::\n",file_text)