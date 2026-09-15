"""Project Euler Problem 83: Path sum: four ways

https://projecteuler.net/problem=83
(Copied verbatim from project_euler.ipynb, cell 83.)
"""

# Problem 83: Path sum: four ways
# here we use A* algorithm, please check the jupyter notebook: ./implementation_A_star.ipynb
from typing import Protocol, Iterator, Tuple, TypeVar, Optional
T = TypeVar("T") # typing.TypeVar: https://docs.python.org/3/library/typing.html
Location = TypeVar("Location")
GridLocation = Tuple[int,int] # typing.Tuple: https://docs.python.org/3/library/typing.html

class Graph(Protocol): # typing.Protocol: https://docs.python.org/3/library/typing.html
    def neighbors(self,id: Location)->list[Location]: pass
def WeightedGraph(Graph):
    def cost(self,from_ide:Location,to_id:Location)->float:pass

class SquareGrid:
    def __init__(self,width:int,height:int) -> None:
        self.width=width
        self.height=height
        self.walls: list[GridLocation]=[]
    def in_bounds(self,id:GridLocation)->bool:
        (x,y)=id
        return (0<=x<self.width) and (0<=y<self.height)
    def passable(self,id:GridLocation)->bool:
        return id not in self.walls
    def neighbors(self,id:GridLocation)->Iterator[GridLocation]: # typing.Iterator: https://docs.python.org/3/library/typing.html
        (x,y)=id
        neighbors = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)] # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results
class GridWithWeights(SquareGrid):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height) # super() in class inheritance: https://realpython.com/python-super/
        self.weights: dict[GridLocation,float]={}
    def cost(self,from_node:GridLocation,to_node:GridLocation)-> float:
        return self.weights.get(to_node,1)  

import heapq # heapq: https://docs.python.org/3/library/heapq.html
class PriorityQueue:
    def __init__(self) -> None:
        self.elements: list[tuple[float,T]]=[]
    def empty(self)->bool:
        return not self.elements
    def put(self,item:T, priority:float):
        heapq.heappush(self.elements,(priority,item))
    def get(self)->T:
        return heapq.heappop(self.elements)[1]

def heuristic(a:GridLocation,b:GridLocation)->float:
    (x1,y1)=a
    (x2,y2)=b
    return abs(x1-x2)+abs(y1-y2)

def a_star_search(graph: WeightedGraph, start: Location, goal: Location, i_val: Optional[int]=0):
    frontier = PriorityQueue()
    frontier.put(start,0)
    came_from: dict[Location, Optional[Location]]={}
    cost_so_far: dict[Location, float]={}
    came_from[start]=None
    cost_so_far[start]=i_val # here we can set up the value for start point
    while not frontier.empty():
        current: Location=frontier.get()
        if current==goal:
            break
        for next in graph.neighbors(current):
            new_cost=cost_so_far[current]+graph.cost(current,next)
            if next not in cost_so_far or new_cost < cost_so_far.get(next,float('inf')):
                cost_so_far[next]=new_cost
                priority = new_cost+heuristic(next,goal)
                frontier.put(next,priority)
                came_from[next]=current
    return came_from, cost_so_far

import numpy as np
f = np.genfromtxt("p083_matrix.txt",dtype=int,delimiter=",")
rowlen,collen=len(f),len(f[0])
m = GridWithWeights(rowlen, collen)
m.weights = {(x,y):f[x,y] for x in range(rowlen) for y in range(collen)}
start, goal = (0,0), (rowlen-1,collen-1)
"""
came_from, cost_so_far = a_star_search(m, start, goal)
### you need to add the first one, as it defaults as the 0
print(cost_so_far[goal]+f[0,0])
"""
came_from, cost_so_far = a_star_search(m, start, goal, f[0,0])
print(cost_so_far[goal])
