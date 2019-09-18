#ELI PRUSHANSKY 160919
def population():
    #This function calculates the future population after a user input amount of years
    years=float(input("How many years from now?"))
    current=int(307357870)
    s=int(years*365*24*60*60)
    newPopulation=int(current+(.094505*s))
    print("New population is: ",newPopulation)

population()
    
    
