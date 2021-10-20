#Elisa Turner
#This program will allow the user to choose from a menu until they choose to
#exit. It will also keep a running total of the charges and add a 7% sales
#tax to calculate the final bill and display the total to the user.



#Define the main function
def main():

    #Declare and Initialize the variables and constants
    menuChoice = choices = 0
    total = finalTotal = currentTotal = taxTotal = 0.0
    SALESTAX = 0.07
    GRANDEICEDPUMPKINSPICE = 4.25
    GRANDEHOTPUMPKINSPICE = 600.25
    ICEDCHAITEA = 3.25
    HOTCHAITEA = 521.50
    CUPCAKEPOP = 2.75
    
    menuChoice = "-2"
    
    #Display the intro
    print(" Welcome to Squarebucks! Hope you're Thirsty! ")
    print("")
    #Loops come before menu options. While loops are pretest 
    while menuChoice != "1" and menuChoice != "2" and menuChoice != "3" and menuChoice != "4" and menuChoice != "5":  

    
    #Display the menu and prices
        print(" Please choose from the following menu: ")
        print(f"1) Grande Iced Pumpkin Spice $4.25 \n2) Grande Hot Pumpkin Spice $600.25 \n3) Iced Chai Tea $3.25 \n4) Hot Chai Tea $521.50 \n5) Cup Cake Pop $2.75 \n6) Done")
        print("")
        #Prompt for a menu choice
        
        menuChoice = input(" Enter your choice here: ") 
        
        #Selection structure of choices
        if menuChoice == "1":
            currentTotal = currentTotal + GRANDEICEDPUMPKINSPICE
            print(" Sounds yummy! Anything else? ")
            print("")
            print(f" Running Total: ${currentTotal}")
            print("")
            menuChoice = "-2"
            
        elif menuChoice == "2":
            currentTotal = currentTotal + GRANDEHOTPUMPKINSPICE
            print(" Yikes....anything else? ")
            print("")
            print(f" Running Total: ${currentTotal}")
            print("")
            menuChoice= "-2"
            
        elif menuChoice == "3":
            currentTotal = currentTotal + ICEDCHAITEA
            print(" Sounds yummy! Anything else? ")
            print("")
            print(f" Running Total: ${currentTotal}")

            print("")
            menuChoice = "-2"
            
        elif menuChoice == "4":
            currentTotal = currentTotal + HOTCHAITEA
            print(" Yikes....anything else? ")
            print("")
            print(f" Running Total: ${currentTotal}")

            print("")
            menuChoice = "-2"

            
        elif menuChoice == "5":
            currentTotal = currentTotal + CUPCAKEPOP
            print(" Sounds yummy! Anything else? ")
            print("")
            print(f" Running Total: ${currentTotal}")

            print("") 
            menuChoice = "-2"
             
        elif menuChoice == "6":
            print("")
            print(f" Alrighty, Heres your total   ")
                        
            #Add choices together
            print("")    
            print(f" Your Total without tax is ${currentTotal:,.2f}")
            print("")
                
            #Calculate sales tax
            finalTotal = ( currentTotal * SALESTAX ) + currentTotal 
            taxTotal = finalTotal - currentTotal
            print(f" Your tax amount is ${taxTotal:,.2f} ")
            print("")
                
            #Display total bill
            print(f" Your final total is ${finalTotal:,.2f} ")
            print("")
            break

        else:
            print(" Sorry, Pleae enter a number from 1 - 6")
            print("") 
            
 

    

#Display outro
    
    print(" By the way, hot drinks cost more because they suck :), enjoy your drinks!")
    print("")
#Define main again
main()
