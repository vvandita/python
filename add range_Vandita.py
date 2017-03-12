print("Start of program")
x = input('Enter first number of the range:')
x = int(x)
y = input('Enter second number of the range:')
y = int(y)
i = 0
j = 0
for w in range(x,y+1):
    i = i + w
    j = j+1
print("the sum of all the numbers in the range is",i)
print("The number of iterations is ",j)

print("End of program")
