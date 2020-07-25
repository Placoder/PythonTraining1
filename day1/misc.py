import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

print(abs.__doc__)

str = "Plaban"
word = "234"
print(str[:2] + word + str[2:])


print(13 // 5)