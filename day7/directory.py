# https://adventofcode.com/2022/day/7

import os, time

dirMap = {}

#read input file and create all folders and files as needed

def buildFileSystem( fileObject ):
    lines = fileObject.readlines()
    for line in lines:
        args = line.split()
    
        if line.startswith( '$ cd' ):
            print(f"cd to {args[2]}")
            if args[2] == "..":
                #move up a folder
                os.chdir("..")
            else:
                if args[2] != "/":
                    os.chdir( args[2] )            
        elif line.startswith( '$ ls' ):
            print( "ls command" )
        elif line.startswith( 'dir' ):
            print(f"creating directory name {args[1]}")
            os.mkdir( args[1] )
        else:
            #create file with size in name and add to map
            currentDir = os.getcwd()
            print(f"Making new file in {currentDir}")
            f = open(args[1], "wb")
            f.seek( int(args[0]) - 1)
            f.write(b"\0")
            f.close()      
    #time.sleep( 0.1 )

# calc size of a directory - calls itself so dirMap dict is global/outside function
def dirSize(path='.'):
    total = 0
    with os.scandir(path) as p:
        for item in p:
            if item.is_file():
                if (str(item.name) != "directory.py" and str(item.name) != "input.txt" and str(item.name) != "input2.txt" and str(item.name) != ".DS_Store"):
                    #print(f"File {item.name} is size {item.stat().st_size}")
                    total += item.stat().st_size
            elif item.is_dir():
                #print(f"Directory {item.path} is size {dirSize(item.path)}")
                #removing part 1
                #if dirSize(item.path) < 100000:
                dirMap.update({item.path:dirSize(item.path)})
                total += dirSize(item.path)
    #print(dirMap)
    return total

inputFile = open( 'input.txt', 'r' )

#uncomment line to build out needed structure and files - only needed once
#buildFileSystem( inputFile )

if __name__ == "__main__":
    
    totalUsedSpace = dirSize('.')
    totalSpace = 70000000
    
    availSpace = totalSpace - totalUsedSpace
    neededAvailSpace = 30000000
    amountNeeded = neededAvailSpace - availSpace
    
    dirsToDelete = {}
    print(f"Total size {totalUsedSpace}" )
    #removing part 1
    #print(f"Size of folders less than 100000 bytes {sum(dirMap.values())}")

    #part 2 - total disk space is 70000000 - need 30000000 unused - find folders to delete and sum those
    
    for dir in dirMap:
        if (dirMap[dir] >= amountNeeded):
            #print(f"Dir {dir} has a size of {dirMap[dir]}")
            dirsToDelete.update({dir:dirMap[dir]})
            
    print( min(dirsToDelete.values()) )
    