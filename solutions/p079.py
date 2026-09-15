"""Project Euler Problem 79: Passcode derivation

https://projecteuler.net/problem=79
(Copied verbatim from project_euler.ipynb, cell 79.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 79: Passcode derivation
### You need to have some basic idea about graph theory ###
from collections import defaultdict
from collections import deque #deque provides O(1) time complexity instead of O(n) in list
#check the web site for more details about deque: https://www.geeksforgeeks.org/deque-in-python/
def find_number_universe(strset):
    numbers = set()
    for attempt in strset:
        for num in attempt:
            numbers.add(num)
    return numbers

### 314: 3 -> [1,4], 1 -> [4] ###
def make_number_graph(strset):
    def connections(attempt):
        l = len(attempt)
        for i in range(l - 1):
            for j in range(i + 1, l):
                yield attempt[i], attempt[j]
    
    graph = defaultdict(set)
    for attempt in strset:
        for a, b in connections(attempt):
            graph[a].add(b)
    return graph

### Breadth-first searching ###
### the algorithm traverses all the nodes of level N and then moves to the nodes of level N+1 ###
### traversing a graph by visiting the nodes in “breadth” than in “depth” ###
### for more details: https://en.wikipedia.org/wiki/Breadth-first_search ###
def find_smallest_code(start, graph, number_universe):
    queue = deque([(start, [start])])
    #print(queue)
    while queue:
        curr, path = queue.popleft()  ### queue.popleft return the thing that has been popped, curr=start, path=[start]
        neighbours = graph.get(curr, [])
        for neighbour in neighbours:
            new_path = path + [neighbour]
            if not number_universe - set(new_path):
                return len(new_path), new_path
            queue.append((neighbour, new_path))

if __name__=="__main__":
    f=open("p079_keylog.txt","r")
    strlist=f.readlines()
    strset=set(content.strip("\n") for content in strlist)
    f.close()
    number_universe = find_number_universe(strset)
    graph = make_number_graph(strset)
    candidates = []
    for vertex in graph:
        code = find_smallest_code(vertex, graph, number_universe)
        if code: candidates.append(code)
    candidates.sort(key=lambda x:x[0])
    print(''.join(candidates[0][1]))
