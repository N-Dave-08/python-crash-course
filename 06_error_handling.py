# 1
try:
    num = int(2)
except ValueError:
    print("not a number")
else:
    print("a number")


# 2
def check_positive(n):
    if n < 0:
        raise ValueError("this is negative")
        return n


try:
    print(check_positive(-1))
except ValueError as e:
    print("Error", e)


# use case
def get_name():
    while True:
        try:
            name = input("Enter you name: ")
            if not name.isalpha():
                raise ValueError("Please enter letter only")
            return name
        except ValueError as e:
            print("Error: ", e)


print(get_name())
