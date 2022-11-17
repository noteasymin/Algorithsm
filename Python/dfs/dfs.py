from inspect import stack
from operator import ne
from pickletools import StackObject


def dfs():
    vertexList = ['0','1','2','3','4','5','6']
    edgeList = [(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(4,6),(5,2),(6,4)]

    adjacencyList =[[] for vertex in vertexList]
    
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
    
    print(adjacencyList)

    stack = [0]
    visitedVertex = []
    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
            visitedVertex.append(current)
    print(visitedVertex)


dfs()