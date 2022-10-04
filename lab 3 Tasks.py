//Activity 1//
class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.totalcost=totalCost
        
graph={'A':Node('A',None,['B','C','E'],None),
       'B':Node('B',None,['A','D','E'],None),
       'C':Node('C',None,['A','F','G'],None),
       'D':Node('D',None,['B','E'],None),
       'E':Node('E',None,['A','B','D'],None),
       'F':Node('F',None,['C'],None),
       'G':Node('G',None,['C'],None)}
print (graph.keys())

//Activity 2//

class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.totalcost=totalCost
def BFS():
    initialState = 'D'
    goalState = 'F'

        
    graph={'A':Node('A',None,['B','C','E'],None),
           'B':Node('B',None,['A','D','E'],None),
           'C':Node('C',None,['A','F','G'],None),
           'D':Node('D',None,['B','E'],None),
           'E':Node('E',None,['A','B','D'],None),
           'F':Node('F',None,['C'],None),
           'G':Node('G',None,['C'],None)}
    
    frontier=[initialState]
    explored=[]
    while len(frontier)!=0:
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent=currentNode
                if graph[child].state==goalState:
                    return actionSequence(graph,initialState,goalState)
                frontier.append(child) 


def actionSequence(graph,initialState,goalState):
    solution=[goalState]
    currentParent=graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent=graph[currentParent].parent
    solution.reverse()
    return solution
solution=BFS()
print(solution)

//TASK 1//

class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.totalcost=totalCost
def BFS():
    initialState = 'arad'
    goalState = 'bush'

        
    graph={'arad':Node('arad',None,['timi','sibi',],None),
           'timi':Node('timi',None,['arad','lugo'],None),
           'sibi':Node('sibi',None,['arad','rici vil','fagaras'],None),
           'fagaras':Node('fagaras',None,['bush','sibi'],None),
           'lugo':Node('lugo',None,['timi','mehadia'],None),
           'rici vil':Node('rici vil',None,['sibi','pitesti'],None),
           'mehadia':Node('mehadia',None,['lugo','dro'],None),
           'pitesti':Node('pitesti',None,['gilurgiu'],None),
        
           'bush':Node('bush',None,['gilurgiu','pitesti','fagaras'],None)}
         
    
    frontier=[initialState]
    explored=[]
    while len(frontier)!=0:
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent=currentNode
                if graph[child].state==goalState:
                    return actionSequence(graph,initialState,goalState)
                frontier.append(child)                


def actionSequence(graph,initialState,goalState):
    solution=[goalState]
    currentParent=graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent=graph[currentParent].parent
    solution.reverse()
    return solution
solution=BFS()
print(solution)




