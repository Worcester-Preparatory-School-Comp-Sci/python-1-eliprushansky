#ELI PRUSHANSKY 160919
def gasoline():
    #This function calculates different measurements of gasoline and its effects with a user input for the amount of gasoline
    gallons=float(input("How many gallons?"))
    liters=float(gallons*3.785)
    barrels=float(gallons/19.5)
    carbonDioxide=float(gallons*20)
    price=float(gallons*3.35)
    print("Number of gallons of gasoline: ",gallons)
    print("Number of liters of gasoline: ",liters)
    print("Number of barrels of oil needed: ",barrels)
    print("Pounds of CO2 produced from this gasoline: ",carbonDioxide)
    print("Price of gasoline: ",price)

gasoline()
