# Covert a file with lines of hex values in "hex.txt" to decimal
# values and write to "dec.txt"

# NOTE: This program only handles Value errors and replaces them
# with the string XXXXX, no other error handling is performed  

HEXLIST_FILENAME = "hex.txt"
DECLIST_FILENAME = "dec.txt"

def loadHex():
    """
    Returns a list of Hex strings from a file
    
    """
    hexList = []
    print "Loading hex list from file..."
    try:
        inFile = open(HEXLIST_FILENAME, 'r', 0)
    except IOError:
        print'No such file "hex.txt"'
        #more error handeling here
    for line in inFile:
        hexList.append(line.strip().upper())
    print len(hexList), "Numbers loaded."
    return hexList

def hexToDec(hexString):
    """
    Takes in a string representing a hex value
    
    Returns a decimal number string
    """
    try:
        i=int(hexString,16)
    except ValueError:
        print'Oops! There was an invalid number in hex.txt...'
        print'Invalid number replaced with XXXXX'
        i='XXXXX'
    return str(i/float(2**21))

def exportDec(decList):
    """


    """
    outFile=open(DECLIST_FILENAME,'w',0)
    for num in decList:
        outFile.write(num+"\n")

    outFile.close()
    print "Success! Decimal numbers written to dec.txt"


decList = []
hexVals=loadHex()
for hexnum in hexVals:
    decList.append(hexToDec(hexnum))

exportDec(decList)

s=raw_input('Press Enter to exit...')


