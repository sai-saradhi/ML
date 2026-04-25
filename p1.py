def bfs_search(graph, start, target):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        visited.append(node)
        print(node, end = " ")
        
        if node == target:
            print(f"\nFound {target}")
            return True
        
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                
    print(f"\n{target} not found")
    return False

# user input
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# graph={}
# n = int(input("Enter number of nodes: "))
        
# for i in range(n):
#     node = input("Enter node name: ")
#     neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
#     graph[node] = neighbors
    
start = input("Enter the starting node: ")
target = input("Enter the Target node: ")

bfs_search(graph,start,target)