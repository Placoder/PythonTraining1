def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return x * calc_factorial(x-1)


num = 4
print("The factorial of", num, "is", calc_factorial(num))


# filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)


# double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)