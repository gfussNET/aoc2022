
#subtract these values from ASCII char value to map priorities:  a = 1, b = 2, c = 3...A = 27, B = 28, C = 29
lowercaseASCII = 96
uppercaseASCII = 38

itemTypePrioritySum = 0

inputFile = open( 'input.txt', 'r')

lines = inputFile.readlines()


for line in lines:
    line.strip() #remove newline/white space
    ruckCompartmentA = line[:len(line)//2]
    ruckCompartmentB = line[len(line)//2:]
    
    #print(f"CompA {ruckCompartmentA}\nCompB {ruckCompartmentB}")
    
    #find common rucksack items (characters)
    itemTypeMatch = set(ruckCompartmentA).intersection(ruckCompartmentB)
    itemType = list(itemTypeMatch)[0]

    if (itemType.isupper()):
        itemTypePrioritySum += ord(itemType) - uppercaseASCII
    else:
        itemTypePrioritySum += ord(itemType) - lowercaseASCII

    #print(f"Item Type Match: {itemTypeMatch}, Item Type Priority: {itemTypePriority}")

print(f"Sum of item priorities: {itemTypePrioritySum}")


#part 2 - collect 3 elve's rucksack items - find common item and score priority keeping running summation
rucksacks = []
itemTypePrioritySum = 0

for line in lines:
    rucksacks.append( line.strip() )
    if len(rucksacks) >= 3: #we have a group of 3, find sommon item type and score it
        itemTypeMatch = set.intersection( *map( set,rucksacks ) )
        
        itemType = list(itemTypeMatch)[0]

        if (itemType.isupper()):
            itemTypePrioritySum += ord(itemType) - uppercaseASCII
        else:
            itemTypePrioritySum += ord(itemType) - lowercaseASCII
        
        print(f"Common item in {rucksacks} is {itemTypeMatch}")
        rucksacks = []
print(f"Sum of item priorites across 3 rucksacks: {itemTypePrioritySum}")