#ELI PRUSHANSKY 160919
def spread():
    #This function calculates the depth of great lake water if spread out on 48 states
    waterVolumeCubicMiles=int(5472)
    areaStatesSquareMiles=int(3119884)
    depthOfWaterMiles=round(waterVolumeCubicMiles/areaStatesSquareMiles,6)
    print(depthOfWaterMiles, " miles deep")
    print(depthOfWaterMiles*5280, " feet deep")

spread()
