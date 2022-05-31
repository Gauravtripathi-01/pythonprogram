Number_of_Heads=int(input("Enter the number of heads : "))
Number_of_legs=int(input("Enter the number of legs : "))
if Number_of_Heads>Number_of_legs:
    print("It is impossible to define the number of Chicken and Goats ")
else: 
    Number_of_chicken=int((4*Number_of_Heads-Number_of_legs)/2)
    Number_of_Goats=int(Number_of_Heads-Number_of_chicken)
    print("Number of Chickens = ",Number_of_chicken)
    print("Number of Goats= ",Number_of_Goats)