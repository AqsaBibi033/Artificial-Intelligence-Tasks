              #Uniform Cost Search
              #Activity 1
import math

class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        

def FindMin(frontier):
    minValue = math.inf
    node = ''
    for i in frontier:
        if minValue > frontier[i][1]:
            minValue = frontier[i][1]
            print(i)
            node = i
    return node

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution


def UCS():
    initialState = 'D'
    goalState = 'G'
    
    graph = {'A': Node('A', None, [('B',6), ('C',9), ('E',1)], 0),
             'B': Node('B', None, [('A',6), ('D',3), ('E',4)], 0),
             'C': Node('C', None, [('A',9), ('F',2), ('G',3)], 0),
             'D': Node('D', None, [('B',3), ('E',5), ('F',7)], 0),
             'E': Node('E', None, [('A',1), ('B',4), ('D',5), ('F',6)], 0),
             'F': Node('F', None, [('C',2), ('E',6), ('D',7)], 0),
             'G': Node('G', None, [('C',3)], 0)}
    frontier = dict()
    frontier[initialState] = (None, 0)
    explored = []
    
    while len(frontier) != 0:
        currentNode = FindMin(frontier)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)
        explored.append(currentNode)
        
        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalCost
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)
            elif child[0] in frontier:
                if frontier[child[0]][1] < currentCost:
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]
                else:
                    frontier[child[0]] = (currentNode, currentCost)
                    graph[child[0]].totalCost = frontier[child[0]][1]
                    
sol = UCS()
print(f"Shortest path is: {sol}")



                  #Tasks1
import math

class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        

def FindMin(frontier):
    minValue = math.inf
    node = ''
    for i in frontier:
        if minValue > frontier[i][1]:
            minValue = frontier[i][1]
            print(frontier[i])
            node = i
    return node

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution


def UCS():
    initialState = 'Arad'
    goalState = 'Bucharest'
    
    graph = {'Oreadea': Node('Oreadea', None, [('Zerind',71), ('Sibiu',151)], 0),
             'Zerind': Node('Zerind', None, [('Oreadea',71), ('Arad',75)], 0),
             'Sibiu': Node('Sibiu', None, [('Oreadea',151), ('Arad',140), ('Fagaras',99)], 0),
             'Arad': Node('Arad', None, [('Zerind',75), ('Sibiu',140), ('Timisoara',118)], 0),
             'Fagaras': Node('Fagaras', None, [('Sibiu',99), ('Bucharest',211)], 0),
             'Timisoara': Node('Timisoara', None, [('Arad',118), ('Lugoj',111)], 0),
             'Rimnicu': Node('Rimnicu', None, [('Sibiu',80), ('Pitesti',97), ('Craiova',146)], 0),
             'Lugoj': Node('Lugpj', None, [('Timisoara',111), ('Mehadia',70)], 0),
             'Pitesti': Node('Pitesti', None, [('Rimnicu',97), ('Craiova', 138), ('Bucharest', 101)], 0),
             'Mehadia': Node('Mehadia', None, [('Lugoj',70), ('Drobeta',75)], 0),
             'Bucharest': Node('Bucharest', None, [('Fagaras', 211), ('Pitesti',101), ('Giurgiu', 90)], 0),
             'Neamt': Node('Neamt', None , [('Iasi',87)], 0),
             'Iasi': Node('Iasa', None, [('Neamt', 87), ('Vaslui',92)], 0),
             'Vaslui': Node('Vaslui', None, [('Iasi',92), ('Urziceni',142)], 0),
             'Urziceni': Node('Urziceni', None, [('Vaslui',142), ('Bucharest',85), ('Hirsova', 98)], 0),
             'Hirsova': Node('Hirsova', None, [('Urziceni',98), ('Eforie',86)], 0),
             'Eforie': Node('Eforie', None ,[('Hirsova',86)], 0),
             'Drobeta': Node('Drobeta', None, [('Mehadia',75), ('Craiova',120)], 0),
             'Craiova': Node('Craiova', None, [('Drobeta',120), ('Pitesti',138), ('Rimnicu', 146)], 0),
             'Giurgiu': Node('Giurgiu', None, [('Bucharest',90)], 0)}

    frontier = dict()
    frontier[initialState] = (None, 0)
    explored = []
    
    while len(frontier) != 0:
        currentNode = FindMin(frontier)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)
        explored.append(currentNode)
        
        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalCost
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)
            elif child[0] in frontier:
                if frontier[child[0]][1] < currentCost:
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]
                else:
                    frontier[child[0]] = (currentNode, currentCost)
                    graph[child[0]].totalCost = frontier[child[0]][1]
                    
sol = UCS()
print(f"Shortest path is: {sol}")
