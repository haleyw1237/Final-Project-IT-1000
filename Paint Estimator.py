


def askForWallSpace():
    userWallSpace = float( input( "Please enter the square feet of wallspace"+ \
                                  " to be painted: " ))
    print()
    return userWallSpace

def askForPriceOfPaint():
    priceOfPaint = float( input( "Please enter the price of the paint: "))
    print()
    return priceOfPaint

def calculatePaintRequired( userWallSpace ):
    paintRequired = ( userWallSpace / 112 )*1
    return paintRequired
    

def calculateHoursOfLaborRequired( userWallSpace ):
    hoursRequired = (userWallSpace / 112)*8
    return hoursRequired

def calculateCostOfPaint( priceOfPaint, gallonsOfPaintRequired ):
    CostOfPaint = gallonsOfPaintRequired * priceOfPaint
    return CostOfPaint

def calculateLaborCharges(hoursOfLaborRequired):
    CHARGE_PER_HOUR = 35.00
    LaborCharges = hoursOfLaborRequired * CHARGE_PER_HOUR
    return LaborCharges

def calculateTotalCostOfPaintJob( LaborCharges, CostOfPaint):
    totalCost = LaborCharges + CostOfPaint
    return totalCost

def printBill( paintRequired, hoursRequired, CostOfPaint, LaborCharges,
               totalCost ):
    print( "Paint required: " + format( paintRequired, ".2f"))
    print( "Hours of Labor required: " + format(hoursRequired, ".2f"))
    print( "Cost of the paint: $ " + format(CostOfPaint, ".2f"))
    print( "Labor charges: $" + format(LaborCharges, ".2f"))
    print( "totalCost: $" + format(totalCost, ".2f"))
    
    

def main():
    userWallSpace = askForWallSpace()
    priceOfPaint = askForPriceOfPaint()
    paintRequired = calculatePaintRequired( userWallSpace)
    hoursRequired = calculateHoursOfLaborRequired( userWallSpace)
    CostOfPaint = calculateCostOfPaint( priceOfPaint, paintRequired)
    LaborCharges = calculateLaborCharges( hoursRequired)
    totalCost = calculateTotalCostOfPaintJob( LaborCharges, CostOfPaint)
    printBill( paintRequired, hoursRequired, CostOfPaint, LaborCharges,
               totalCost)
main()
    
