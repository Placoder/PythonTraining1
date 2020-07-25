


# dic = {
#     "firstName": "Rahul",
#     "lastName": "Mane",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Pallavi",
#             "age": 6
#         },
#         {
#             "firstName": "Sanket",
#             "age": 8
#         }
#     ]
# }
# print("Age of ",dic["children"][0]["firstName"]," is ",dic["children"][0]["age"])

def even(x):
    while (x != 0):
        if x % 2 == 0:
            yield x
        x -= 1
for i in even(8):
    print(i)

iter_obj=iter([3,4,5])


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Plaban")


