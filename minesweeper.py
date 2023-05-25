import copy


# define a function and use 'grid' as parameter
def mine_sweeper(grid):

    # get the number of rows and columns in the 2D list
    row = len(grid)
    col = len(grid[0])

    # generate a new 2D list that has same size and items compared with 'grid'
    new_grid = copy.deepcopy(grid)

    # iterate all items in the 2D list 'grid'
    for i in range(row):
        for j in range(col):

            # count number of '#' adjacent to each '-'
            if grid[i][j] == "-":
                count = 0
                for r in range(i-1, i+2):
                    for c in range(j-1, j+2):

                        # exclude the current location, and when the adjacent location is within the grid and item is '#', couter plus one
                        if (r != i or c != j) and r >= 0 and r < row and c >= 0 and c < col and grid[r][c] == "#":
                            count += 1

                # replace the current location with the number of adjacent '#'
                new_grid[i][j] = str(count)

    # return the new 2D list
    return new_grid


# ask user input a qualified 2D list defensively
while True:
    try:
        grid = []
        while True:
            row = input("Please input a row of content, only include '-' and '#'. Input 'q' to finish: ")
            if row == 'q':
                if not grid:
                    print("The input grid is empty. Please re-enter.")
                    continue
                else:
                    break
            else:

                # check each character in input line whether it is qualified
                if not all(c in ('-', '#', 'q') for c in row):
                    print("The input format is incorrect. Please only use '-' and '#' and 'q' characters.")
                    continue
                grid.append(list(row))

                # check if each line has same length
                if len(grid[-1]) != len(grid[0]):
                    print("The input format is incorrect. All rows should have the same length.")
                    grid.pop()
        break
    except ValueError:
        print("The input format is incorrect. Please re-enter.")

# calculate the new 2D list by using the defined function
new_grid = mine_sweeper(grid)

# print out the original 2D list and new 2D list
print()
print("The original grid you input is: ")
for row in grid:
    print(' '.join(row))

print()
print("The new grid is: ")
for row in new_grid:
    print(' '.join(row))
