import random
import time

# Merge function
def merge(arr, left, mid, right):
    leftArr = arr[left:mid + 1]
    rightArr = arr[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1

# Merge sort function
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Generate average-case input
def generate_random_array(size):
    return [random.randint(0, 99) for _ in range(size)]

# Generate best-case input
def generate_sorted_array(size):
    return list(range(size))

# Generate worst-case input (reverse sorted)
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

# Main
def main():
    sizes = [100, 500, 1000, 5000, 10000]
    for size in sizes:
        print(f"\nArray Size: {size}")

        # Average case
        arr = generate_random_array(size)
        start = time.time()
        merge_sort(arr, 0, size - 1)
        end = time.time()
        print(f"Average case: {end - start:.6f} seconds")

        # Best case
        arr = generate_sorted_array(size)
        start = time.time()
        merge_sort(arr, 0, size - 1)
        end = time.time()
        print(f"Best case:    {end - start:.6f} seconds")

        # Worst case
        arr = generate_reverse_sorted_array(size)
        start = time.time()
        merge_sort(arr, 0, size - 1)
        end = time.time()
        print(f"Worst case:   {end - start:.6f} seconds")

if __name__ == "__main__":
    main()
