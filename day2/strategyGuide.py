#Play Mapping
#A:X - Rock (1) - X: Lose
#B:Y - Paper (2) - Y: Draw
#C:Z - Scissors (3) Z: Win

#Modifiers
#Win = 6
#Draw = 3
#Loss = 0

pointValue = { 'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

def rpsShoot( play, response ):
    roundScore = 0
    #get vaule of object played and add to round score
    roundScore = pointValue[response]
    #add modifier for win or draw
    if pointValue[play] == pointValue[response]:
        roundScore += 3 #draw
    if play == 'A' and response == 'Y':
        roundScore += 6 #win
    if play == 'B' and response == 'Z':
        roundScore += 6 #win
    if play == 'C' and response == 'X':
       roundScore += 6 #win
    return roundScore

def rpsDefend( play, outcome ):
    
    winDict = {'A':'Y', 'B':'Z', 'C':'X'}
    loseDict = {'A':'Z', 'B':'X', 'C':'Y'}
    drawDict = {'A':'X', 'B':'Y', 'C':'Z'}

    if outcome == 'X': #we are supposed to lose
       return loseDict[play]   
    if outcome == 'Y': #we need to draw
       return drawDict[play]
    if outcome == 'Z': #WINNER WINNER
       return winDict[play]


inputFile = open( 'puzzleGuide.txt', 'r')
lines = inputFile.readlines()
runningScore = 0

for line in lines:
    # split line to get play and response
    play, response = line.split()

    # calculate who won, score for round and update running total
    runningScore += rpsShoot( play, response) 
      

print(f"Total score was {runningScore}") 

#part 2
runningScore = 0

for line in lines:
    # split line to get play and outcome
    play, outcome = line.split()

    # calculate who won, score for round and update running total
    response = rpsDefend( play, outcome)

    runningScore += rpsShoot( play, response) 

print(f"Total score was {runningScore}") 
