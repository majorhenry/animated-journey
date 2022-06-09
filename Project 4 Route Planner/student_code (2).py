# start - The "start" node for the search algorithm.
# goal - the "goal" node.
# path - an array of integers corresponding to valid intersection access sequences on the map.
# Ex: start=5, goal=34, path=[5,16,37,12,34]
from math import sqrt 

def shortest_path(M,start,goal):
    # The dictionary of the intersections of M
    nodes=M.intersections
    
    # The list that shows the connectivity of M
    roads=M.roads
    
    # The set of nodes already explored
    visited=set()
    
    # The set of intersections that are going to be explored
    visit=set()
    visit.add(start)
    
    
    # The dict that cantains the most efficient Parent node of every node
    Parent={}
    
    # For each node, the cost of getting from the start node to that node.
    gScore={start:0}
    
    # For each node, the total cost of getting from the start node to the goal
    value=calcH(nodes[start], nodes[goal])
    f_Score={start:value}
    
    while len(visit) is not 0:
        
        current = min(visit, key=f_Score.get)
        if current == goal:
            return rebuild(Parent, current)

        visit.remove(current)

        visited.add(current)
        
        for neighbor in roads[current]:
            if neighbor in visited:
                continue
                
            #gScore[neighbor] = calcG(nodes[current], nodes[neighbor])
            indefinite_gScore = gScore[current] + calcG(nodes[current], nodes[neighbor])
            if neighbor not in visit:
                visit.add(neighbor)
            elif indefinite_gScore >= gScore[neighbor]:
                continue
            gScore[neighbor] = indefinite_gScore
            Parent[neighbor] = current
            f_Score[neighbor] = gScore[neighbor] + calcH(nodes[neighbor], nodes[goal])
        
    # print("shortest path called")
    return False

def calcG(node1, node2):
    return sqrt(abs((node1[0]-node2[0])*2+(node1[1]-node2[1])*2))

def calcH(node1, end):
    return sqrt(abs((node1[0]-end[0])*2+(node1[1]-end[1])*2))

def rebuild(Parent, current):
    full_path = [current]
    while current in Parent.keys():
        current = Parent[current]
        full_path.append(current)
    full_path.reverse()
    return full_path