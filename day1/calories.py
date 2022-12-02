
elves = []
calCount = 0
inputFile = open( 'input.txt', 'r')

lines = inputFile.readlines()


for line in lines:
    if line.strip():
       calCount += int(line.strip())
    else:
        elves.append( calCount )
        calCount = 0

    
#Find most calories
sortedCals = sorted(elves, reverse=True)

print(f"Most cals: {sortedCals[0]}" )
sumCals = sum(sortedCals[0:3])
print(f"Top 3 total cals: {sumCals}")  


