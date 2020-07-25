import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except (ZeroDivisionError):
        print("Oops! ZeroDivisionError occured.")
        print("Next entry.")
        print()
    # except:
    #     print("Oops!",sys.exc_info()[0],"occured.")
    #     print("Next entry.")
    #     print()
    except Exception as e:
        print("Oops! Exception occured : ",e)
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)