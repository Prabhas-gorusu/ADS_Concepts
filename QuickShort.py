import random
import time

# Function to swap elements (not needed in Python, handled inline)

# Partition function for Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

# Generate random array (average case)
def generate_random_array(size):
    return [random.randint(0, 99) for _ in range(size)]

# Generate sorted array (best case for some pivot strategies)
def generate_sorted_array(size):
    return list(range(size))

# Generate reverse sorted array (worst case for some pivot strategies)
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

# Main execution
def main():
    sizes = [100, 500, 1000, 5000, 10000]
    for size in sizes:
        print(f"\nArray Size: {size}")
        
        # Average case
        arr = generate_random_array(size)
        start = time.time()
        quick_sort(arr, 0, size - 1)
        end = time.time()
        print(f"Average case: {end - start:.6f} seconds")
        
        # Best case
        arr = generate_sorted_array(size)
        start = time.time()
        quick_sort(arr, 0, size - 1)
        end = time.time()
        print(f"Best case:    {end - start:.6f} seconds")
        
        # Worst case
        arr = generate_reverse_sorted_array(size)
        start = time.time()
        quick_sort(arr, 0, size - 1)
        end = time.time()
        print(f"Worst case:   {end - start:.6f} seconds")

if __name__ == "__main__":
    main()
