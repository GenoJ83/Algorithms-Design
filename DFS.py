def dfs_stack(graph, start):
    # Set to keep track of visited nodes
    visited = set()
    # Stack to manage nodes to be explored; initialized with the start node
    stack = [start]
    
    # Iterate until there are nodes to process in the stack
    while stack:
        # Pop the last node from the stack (LIFO order)
        node = stack.pop()
        
        # If the node has not been visited, process it
        if node not in visited:
            # Print the node (or perform any desired operation)
            print(node, end="")
            # Mark the node as visited
            visited.add(node)
            
            # Add all unvisited neighbors to the stack in reversed order
            # Reversing ensures proper DFS traversal order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    "A": ["S", "D"],
    "B": ["D", "S"],
    "S": ["A", "B", "C"],
    "D": ["A", "B", "C"],
    "C": ["S", "D"],
}

# Perform DFS starting from node "S"
dfs_stack(graph, "S")
