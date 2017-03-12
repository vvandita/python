print("start of program" )

x = input("enter first number: ")
x = int(x)
y = input("enter second number: ")
y = int(y)


for w in range(x,y+1):

    if(w % 3 == 0):
        print("Fizz")
        
    
    if(w % 5 == 0):
        print("Buzz")

    if(w % 3 == 0) and (w % 5 == 0):
        print("FizzBuzz")


    else:
        print(w)



        
