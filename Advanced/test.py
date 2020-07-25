def calcDigit(n):
    length = len(str(n))
    if length > 1:
        return pow(10,length-1)
    else:
        return 1
# x = 120
# print(x/calcDigit(199))

# check digit present fun
def isDigitPresent(x, d):
    # Break if d is present as digit
    while (x > 0):
        if (x % 10 == d):
            break
        if (x / calcDigit(x) == d):
            # return if any other digit becomes d intead of last digit
            return
        x = x / 10
    return (x > 0)

# display the values fun
def printNumbers(n, d):
    # numbers one by one
    for i in range(0, n + 1):
        # check if digit
        if (i == d or isDigitPresent(i, d)):
            print(i, end=" ")

n = 199   # Starts from 0 till this number
d = 1    # Enter the digit to be searched in above sequence
print("The number ending in digit 3 ")
printNumbers(n, d)