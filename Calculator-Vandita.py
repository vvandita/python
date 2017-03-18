def add (a,b):
    result = a + b
    return result

def multiply(a,b):
    result = a*b
    return result


print("Start of program") 

number1 = input("Enter the first number: ")
number1 = int(number1)
number2 = input("Enter the second number:")
number2 = int(number2)

selection = input("Would you like to + or *: ")


if(selection == "+"):
    answer = add(number1,number2)
    print(number1, "+",number2, "=", answer)

if(selection == "*"):
    answer = multiply(number1,number2)
    print(number1, "*" ,number2, "=", answer)

print("End of program ****")

