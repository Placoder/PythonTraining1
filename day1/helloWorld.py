import re
#First Program
# user = input("CEC ID:")
# print("Hello ",user, " welcome to Python World\n")


def test(*args):
    for data in args:
        if isinstance(data, str): print(data)
        if isinstance(data, int): print(data)
    print("In function")
data = '\"paths\": [\"/WEB-INF/lib/acegi-security-1.0.7.jar\", \"war/target/jenkins/WEB-INF/lib/acegi-security-1.0.7.jar\"], \"usages\": [\"DYNAMICALLY_LINKED\"], \"license\": \"Apache License 2.0\"'
data = re.sub(r"\\+\"","",data)
# print(data)
test(100)
test(data)


