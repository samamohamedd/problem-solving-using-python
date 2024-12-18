def max_heapify(arr, n, i): 
    # Find the largest among root, left child, and right child
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest) 

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        max_heapify(arr, i, 0)

#The outer loop runs O(n) times, and each MAX_HEAPIFY call takes 𝑂(log⁡𝑛)O(logn). so, the sorting phase takes 𝑂(𝑛log⁡𝑛)