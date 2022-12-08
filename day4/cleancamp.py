


inputFile = open( 'input.txt', 'r')

lines = inputFile.readlines()
duplicatedEffort = 0
overlappingSections = 0

for line in lines:
    line.strip() #remove newline/white space
    sectionA, sectionB = line.split(",")

    #build integer lists from the range provided
    sectionARange = sectionA.split("-")
    sectionAList = list( range( int(sectionARange[0]), int(sectionARange[1])+1 ) ) 
    
    sectionBRange = sectionB.split("-")
    sectionBList = list( range( int(sectionBRange[0]), int(sectionBRange[1])+1 ) ) 
    
    if( set(sectionAList).issubset(set(sectionBList)) or set(sectionBList).issubset(set(sectionAList))):
        duplicatedEffort += 1
    
    #part 2: do any assignment pairs overlap
    if( set(sectionAList) & set(sectionBList)):
        overlappingSections += 1
    
    sectionAList = []
    sectionBList = []
    
print(f"Duplicated Effort total: {duplicatedEffort}\n Overlapping Total: {overlappingSections}")
    

