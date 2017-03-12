print("Start of program")
count = 0                    #making a index name or variable
inputList = [""]*100         #initializing the name of the list
num = input("Enter a number or quit:")
#inputList = [""]*len(word)
while(num != "quit"):
    num = int(num)             
    inputList[count] = num    #populat ing the list(or putting the inputs into the list)
    count = count + 1         #increasing the count by 1(iteration)
    num = input("Enter a number or quit:")
print(inputList)              #printing the list
print("End of program")
