###############################################################################################################################################
## he dfs function recursively performs Depth-First Search starting from the start node.
## The graph is represented as an adjacency list.
## The function recursively visits each neighbor of a node until it reaches the 'goal' node or all reachable nodes are visited.
## Ensure to adjust the 'graph', 'start_node', and 'goal_node variables based on your specific graph structure and nodes.
###############################################################################################################################################

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    if start == goal:
        return True

    for neighbor in graph[start]: 
        if neighbor not in visited: 
            if dfs(graph, neighbor, goal, visited): 
                return True

    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

start_node = 'A'
goal_node = 'D'

result = dfs(graph, start_node, goal_node)
print("Path exists:", result)
