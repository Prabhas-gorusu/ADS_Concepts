from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src)  # Since the graph is undirected

    def BFT(self, start_vertex):
        visited = [False] * self.num_vertices
        queue = deque()
        queue.append(start_vertex)
        visited[start_vertex] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbor in self.adjacency_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

    def DFTUtil(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")
        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                self.DFTUtil(neighbor, visited)

    def DFT(self, start_vertex):
        visited = [False] * self.num_vertices
        self.DFTUtil(start_vertex, visited)

def main():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = Graph(num_vertices)

    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        src, dest = map(int, input(f"Enter edge {i + 1} (src dest): ").split())
        graph.add_edge(src, dest)

    start_vertex = int(input("Enter the start vertex: "))
    print("Breadth-First Traversal: ", end="")
    graph.BFT(start_vertex)
    print("Depth-First Traversal: ", end="")
    graph.DFT(start_vertex)

if __name__ == "__main__":
    main()
