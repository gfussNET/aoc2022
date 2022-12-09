# starting crate stacks - make moves based upon input.txt
#
# [S]                 [T] [Q]        
# [L]             [B] [M] [P]     [T]
# [F]     [S]     [Z] [N] [S]     [R]
# [Z] [R] [N]     [R] [D] [F]     [V]
# [D] [Z] [H] [J] [W] [G] [W]     [G]
# [B] [M] [C] [F] [H] [Z] [N] [R] [L]
# [R] [B] [L] [C] [G] [J] [L] [Z] [C]
# [H] [T] [Z] [S] [P] [V] [G] [M] [M]
#  1   2   3   4   5   6   7   8   9 

import time

#Move X number of crates from source stack to destination stack
#part2 - updated to just move a single crate
def moveCrate( source, destination ):
    crate = crateStacks[ source-1 ].pop()
    crateStacks[ destination-1 ].append( crate )
    print(f"Moving {crate} from {source} to {destination}")    

#part2 - move crates in whole, keeping order, when more than 1 crate needs moved
def moveCrate9001( quantity, source, destination ):
    if quantity == 1: #just move it like before
        moveCrate( source, destination )
    elif quantity > 1:
        #get slice/stack of crates to move to destination
        cratesToMove = crateStacks[ source-1 ][len(crateStacks[ source-1 ])-quantity:]
        
        #remove from source stack
        del crateStacks[ source-1 ][len(crateStacks[ source-1 ])-quantity:]

        for crate in cratesToMove: #drop them off to new stack
            crateStacks[ destination-1 ].append( crate )
        
        print(f"Crates moving: {cratesToMove} \nSource stack: {crateStacks[ source-1 ]} \nDestination stack: {crateStacks[ destination-1 ]}" )

# create initial stacks
stack1 = [ 'H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S' ]
stack2 = [ 'T', 'B', 'M', 'Z', 'R' ]
stack3 = [ 'Z', 'L', 'C', 'H', 'N', 'S' ]
stack4 = [ 'S', 'C', 'F', 'J' ]
stack5 = [ 'P', 'G', 'H', 'W', 'R', 'Z', 'B' ]
stack6 = [ 'V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T' ]
stack7 = [ 'G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q' ]
stack8 = [ 'M', 'Z', 'R' ]
stack9 = [ 'M', 'C', 'L', 'G', 'V', 'R', 'T' ]

#create list of all stacks
crateStacks = [ stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9 ]

inputFile = open( 'input.txt', 'r')
lines = inputFile.readlines()

for line in lines:
    # split line to get qty, src and dst
    workOrder = line.split()
    numCrates = workOrder[1]
    sourceStack = workOrder[3]
    destStack = workOrder[5]
    
    moveCrate9001( int(numCrates), int(sourceStack), int(destStack) )

    #time.sleep( 15 )
    
for crateStack in crateStacks:
    print(f"Top crate:  {crateStack[-1]}")
   