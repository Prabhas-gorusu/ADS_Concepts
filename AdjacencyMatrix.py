from collections import deque

def BFT(graph, num_vertices, start_vertex):
    visited = [False] * num_vertices
    queue = deque()
    queue.append(start_vertex)
    visited[start_vertex] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for i in range(num_vertices):
            if graph[vertex][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
    print()

def DFTUtil(graph, num_vertices, vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for i in range(num_vertices):
        if graph[vertex][i] == 1 and not visited[i]:
            DFTUtil(graph, num_vertices, i, visited)

def DFT(graph, num_vertices, start_vertex):
    visited = [False] * num_vertices
    DFTUtil(graph, num_vertices, start_vertex, visited)

def main():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = []

    print("Enter the adjacency matrix:")
    for _ in range(num_vertices):
        row = list(map(int, input().split()))
        graph.append(row)

    start_vertex = int(input("Enter the start vertex: "))

    print("Breadth-First Traversal: ", end="")
    BFT(graph, num_vertices, start_vertex)

    print("Depth-First Traversal: ", end="")
    DFT(graph, num_vertices, start_vertex)

if __name__ == "__main__":
    main()
