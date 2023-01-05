                              #Iterative deepening search
                                   #Activity 1
def iterative_deepening_dfs(start, target):

    
    # Start by doing DFS with a depth of 1, keep doubling depth until we reach the "bottom" of the tree or find the node we're searching for
    depth = 1
    print(start)
    bottom_reached = False  # Variable to keep track if we have reached the bottom of the tree
    while not bottom_reached:
        # One of the "end nodes" of the search with this depth has to still have children and set this to False again
        result, bottom_reached = iterative_deepening_dfs_rec(start, target, 0, depth)
        if result is not None:
            # We've found the goal node while doing DFS with this max depth
            return result

        # We haven't found the goal node, but there are still deeper nodes to search through
        depth *= 2
        print("Increasing depth to " + str(depth))

    # Bottom reached is True.
    # We haven't found the node and there were no more nodes that still have children to explore at a higher depth.
    return None


def iterative_deepening_dfs_rec(node, target, current_depth, max_depth):
    print("Visiting Node " + str(node["value"]))

    if node["value"] == target:
        # We have found the goal node we we're searching for
        print("Found the node we're looking for!")
        return node, True

    if current_depth == max_depth:
        print("Current maximum depth reached, returning...")
        # We have reached the end for this depth...
        if len(node["children"]) > 0:
            # ...but we have not yet reached the bottom of the tree
            return None, False
        else:
            return None, True

    # Recurse with all children
    bottom_reached = True
    for i in range(len(node["children"])):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(node["children"][i], target, current_depth + 1,
                                                                 max_depth)
        if result is not None:
            # We've found the goal node while going down that child
            return result, True
        bottom_reached = bottom_reached and bottom_reached_rec

    # We've gone through all children and not found the goal node
    return None, bottom_reached

start={"value": 0, "children":[
   {"value": 1, "children":[
     {"value": 3, "children":[  ]},
     {"value": 4, "children":[ ]}
     ]}, {
         "value": 2, "children":[
             {"value": 5, "children":[ ]},
             {"value": 6, "children":[ ]}
             ]
         }
   ]
}


print(iterative_deepening_dfs(start, 6) ["value"])




                                         # Task 2
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]


# Function to check if it is safe to go to cell (x, y) from the current cell.
# The function returns false if (x, y) is not valid matrix coordinates
# or cell (x, y) is already processed.
def isSafe(x, y, processed):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0])) \
           and not processed[x][y]


# A recursive function to generate all possible words in a boggle
def searchBoggle(board, words, result, processed, i, j, path=''):
    # mark the current node as processed
    processed[i][j] = True

    # update the path with the current character and insert it into the set
    path += board[i][j]

    # check whether the path is present in the input set
    if path in words:
        result.add(path)

    # check for all eight possible movements from the current cell
    for k in range(len(row)):
        # skip if a cell is invalid, or it is already processed
        if isSafe(i + row[k], j + col[k], processed):
            searchBoggle(board, words, result, processed, i + row[k], j + col[k], path)

    # backtrack: mark the current node as unprocessed
    processed[i][j] = False


def searchInBoggle(board, words):
    # construct a set to store valid words constructed from the boggle
    result = set()

    # base case
    if not board or not len(board):
        return

    # `M × N` board
    (M, N) = (len(board), len(board[0]))

    # construct a boolean matrix to store whether a cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]

    # generate all possible words in a boggle
    for i in range(M):
        for j in range(N):
            # consider each character as a starting point and run DFS
            searchBoggle(board, words, result, processed, i, j)

    return result


if __name__ == '__main__':
    board = [
        ['M', 'S', 'E'],
        ['R', 'A', 'T'],
        ['L', 'O', 'N']
    ]

    words = ['STAR', 'NOTE', 'SAND', 'STONE']

    validWords = searchInBoggle(board, words)
    print(validWords)

