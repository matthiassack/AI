from collections import deque

###############################################################################################################################################
## The 'bfs' function implements the Breadth-First Search algorithm using a queue data structure.
## The 'graph' is represented as an adjacency list
## The function starts the search from the 'start' node and traverses the graph until it reaches the 'goal' node or exhausts all possible paths.
## Modify the 'graph', 'start_node', and 'goal_node' variables according to your specific graph structure and nodes.
###############################################################################################################################################

def bfs (graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == goal:
            return True

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

start_node = 'A'
goal_node = 'D'

result = bfs(graph, start_node, goal_node)
print("Path exists:", result)