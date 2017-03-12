print("start of program")


x = input("enter a vowel: ")
count = 0
while(x != "a")and(x != "e")and(x != "i")and(x != "o")and(x != "u"):
    
    
    if(count == 1):
        print("sorry try again")
    if(count == 2):
        print("umm..try again")
    if(count == 3):
        print("think carefully know")
    if(count == 4):
        print("IM DONE WITH IT")
    if(count == 5):
        print("I give up")
        break
    count = count +1
    x = input("enter a vowel: ")
    
    
if(x == "a" and "e" and "i" and "o" and "u"):
    print("you got it")
    
    print("end of program")
                

    
    

    
    

