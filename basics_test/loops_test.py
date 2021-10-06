

values = [1, 4, 3, 9, 8]

print("using for each loop demo")
# for each loop
for i in values:
    print(i)

print("using for loop with range function: indexing demo")
# for loop with index
length = len(values)
for i in range(length):
    print(values[i])

print("using for while loop demo")
# while loop
index = 0
while index < length:
    print(values[index])
    index = index + 1

a = 10
b = 20

print("if else condition demo")
if a < b:
    print(" a < b")
else:
    print(" a > b")

