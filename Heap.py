class Heap:
    def __init__(self, capacity):
        self.heap = []
        self.size = 0
        self.capacity = capacity

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_min(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_min(smallest)

    def heapify_max(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.heapify_max(largest)

    def insert_min(self, value):
        if self.size == self.capacity:
            print("Heap is full")
            return
        self.heap.append(value)
        index = self.size
        self.size += 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] <= self.heap[index]:
                break
            self.swap(parent, index)
            index = parent

    def insert_max(self, value):
        if self.size == self.capacity:
            print("Heap is full")
            return
        self.heap.append(value)
        index = self.size
        self.size += 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] >= self.heap[index]:
                break
            self.swap(parent, index)
            index = parent

    def delete_min(self, value):
        try:
            index = self.heap.index(value)
        except ValueError:
            print("Element not found")
            return
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        self.heapify_min(index)

    def delete_max(self, value):
        try:
            index = self.heap.index(value)
        except ValueError:
            print("Element not found")
            return
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        self.heapify_max(index)

    def display(self):
        print(" ".join(map(str, self.heap)))


if __name__ == "__main__":
    # Min Heap demonstration
    print("Min Heap:")
    min_heap = Heap(10)
    for val in [10, 20, 30, 40, 50]:
        min_heap.insert_min(val)
    min_heap.display()
    min_heap.delete_min(20)
    print("After deletion:")
    min_heap.display()

    # Max Heap demonstration
    print("\nMax Heap:")
    max_heap = Heap(10)
    for val in [10, 20, 30, 40, 50]:
        max_heap.insert_max(val)
    max_heap.display()
    max_heap.delete_max(20)
    print("After deletion:")
    max_heap.display()
    