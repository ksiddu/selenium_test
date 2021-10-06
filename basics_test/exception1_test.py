
# to check number exceptions
try:
    a = int(input("enter number 1: "))
    b = int(input("enter number 2: "))
    result = a/b
    print(result)
except TypeError as e:
    print("Something went wrong", e)
except ValueError as e:
    print("Enter the correct value", e)
except ZeroDivisionError as e:
    print("Enter the non zero value", e)

# to check file I/O exceptions
try:
    f = open("/Users/siddu.kampli/PycharmProjects/selenium_test/TestData.txt", "r")
    print(f.read())
except FileNotFoundError as e:
    print("File doesn't exist", e)

