import random

def displayNumbers(fileToBeRead ):
    try:
        randomNumbersFile = open( fileToBeRead, "r")

        total = 0
        numberOfRandomNumbers = 0
        line = randomNumbersFile.readline()

        while line != "":
                numberOfRandomNumbers =+ 1
                randomNumber = int(line)
                total =+ randomNumber
                print(randomNumber)
                line = randomNumbersFile.readline()
    except Exception as potentialError:
                print("Error:" , potentialError)
    else:
              print( "The total of all the numbers in the file is"
                     ==str(total) +\
                     " there are" + str( numberOfRandomNumbers) +\
                     " numbers in the file")
              randomNumbersFile.close()
    finally:
            print( "End of program")
def main():
    displayNumbers("randomNumbers.txt")
              
            
        
main()





