# Name: Vaibhav Jain
# 2048 Game

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
    return 0        

# Starting the game
startGame()
