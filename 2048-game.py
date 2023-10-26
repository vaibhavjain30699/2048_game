# Name: Vaibhav Jain
# 2048 Game

import random

#Prints the Grid
def printGrid(grid):
    print ("\n")
    for i in range(len(grid)):
        res = ("\t\t")
        for j in range(len(grid[i])):
            for _ in range(5 - len(grid[i][j])): res += " "
            res += grid[i][j] + " "
        print (res)
        print ("\n")
    return 0


# Rotates the grid in clockwise direction
def rotate(grid):
    return list(map(list, zip(*grid[::-1])))


# This function contains all the logic of the game
def move(grid, dir):
    for i in range(dir): grid = rotate(grid)
    for i in range(len(grid)):
        temp = []
        for j in grid[i]:
            if j != '.':
                temp.append(j)
        temp += ['.'] * grid[i].count('.') 
        for j in range(len(temp) - 1):
            if temp[j] == temp[j + 1] and temp[j] != '.' and temp[j + 1] != '.':
                temp[j] = str(2 * int(temp[j]))
                move.score += int(temp[j])
                temp[j + 1] = '.'
        grid[i] = []
        for j in temp:
            if j != '.':
                grid[i].append(j)
        grid[i] += ['.'] * temp.count('.')
    for i in range(4 - dir): grid = rotate(grid)
    return grid
# This adds a random number to the grid
def addNumber(grid):
    num = random.randint(1, 2) * 2
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    lost = checkForMove(grid)
    lost1 = False
    if grid[x][y] != '.':
        x, y, lost1 = findEmptySlot(grid)
    if not lost1: grid[x][y] = str(num)
    return (grid, lost and lost1)


def checkForMove(grid):
    for i in range(0,4):
        for j in range(0,3):
            if(grid[i][j]==grid[i][j+1]):
                return False

    for i in range(0,3):
        for j in range(0,4):
            if(grid[i][j]==grid[i+1][j]):
                return False

    return True


# This checks for an empty slot where we can add a number
def findEmptySlot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j, False)
    return (-1, -1, True)


def startGame():
    print ("\nWelcome to the 2048 Console world. Let's play!")
    print ("Combine given numbers to get a maximum score.\nYou can move numbers to left, right, top or bottom direction.\n")
    
    # For this program, a 4*4 grid is created
    # This can be extended to more number of grids
    grid = [['.', '2', '.', '.'],
            ['.', '4', '.', '2'],
            ['.', '.', '.', '.'],
            ['2', '.', '2', '4']]

    direction = {'1': 0, '2': 1, '3': 2, '4': 3, 'X': 4}

    printGrid(grid)
    loseStatus = 0
    move.score = 0
    while True:
        tmp = input("\nTo continue, Press 1 for left, 2 for bottom, 3 for right, 4 for top or\nPress X to end the game.\n")
        if tmp in ["1", "2", "3", "4", "X", "x"]:
            dir = direction[tmp.upper()]
            if dir == 4:
                print ("\nFinal score: " + str(move.score))
                break
            else:
                grid = move(grid, dir)
                grid, loseStatus = addNumber(grid)
                printGrid(grid)
                if loseStatus:
                    print ("\nGame Over")
                    print ("Final score: " + str(move.score))
                    break
                print ("\nCurrent score: " + str(move.score))
        else:
            print ("\nInvalid direction, please provide valid movement direction (1, 2, 3, 4).")
    return 0        

# Starting the game
startGame()
