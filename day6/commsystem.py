# https://adventofcode.com/2022/day/6

# locate position in string of text (input file) where the last 4 characters have not repeated

inputFile = open( 'input.txt', 'r')

#read in full communication stream
dataStream = inputFile.read() 

#buffer for characters
charBuffer = []
i = 0

for c in dataStream:
    i += 1
    charBuffer.append( c )
    
    #print( len(charBuffer) )

    if len( charBuffer ) > 14: #we only want 4 total in buffer - part2: changed to 14
        charBuffer.pop( 0 )  

    if len( set( charBuffer ) ) == 14: #if here, we've found the a set of 4 chars that are not repeating - part2: changed to 14
        startOfMessage = i
        break
    

print(f"Start of Message: {startOfMessage}")
