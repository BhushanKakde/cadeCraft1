# Q3. Depth-First Search (DFS) Sample Problem: Implement Depth
# First Search (DFS) to traverse a graph starting from a given vertex. 
# The graph is represented by an adjacency list.  



class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def dfs(self, start_vertex):
        visited = set()
        traversal_order = []

        def dfs_helper(vertex):
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start_vertex)
        return traversal_order


# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')

start_vertex = 'A'
traversal_order = graph.dfs(start_vertex)
print("DFS Traversal Order:", traversal_order)



#



