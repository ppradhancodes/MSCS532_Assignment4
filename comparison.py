import random
import time
import statistics

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def time_sorting_algorithm(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time

def run_comparison(sizes, distributions, num_trials=5):
    algorithms = [
        ("Heapsort", heapsort),
        ("Quicksort", quicksort),
        ("Merge Sort", merge_sort)
    ]

    with open("output.txt", "w") as f:
        for size in sizes:
            f.write(f"\nInput size: {size}\n")
            for dist_name, dist_func in distributions:
                f.write(f"\n{dist_name} distribution:\n")
                for algo_name, algo_func in algorithms:
                    times = []
                    for _ in range(num_trials):
                        arr = dist_func(size)
                        times.append(time_sorting_algorithm(algo_func, arr))
                    avg_time = statistics.mean(times)
                    f.write(f"{algo_name}: {avg_time:.6f} seconds (average of {num_trials} trials)\n")

# Test configurations
sizes = [1000, 10000, 100000]
distributions = [
    ("Sorted", lambda n: list(range(n))),
    ("Reverse sorted", lambda n: list(range(n, 0, -1))),
    ("Random", lambda n: [random.randint(1, 1000000) for _ in range(n)])
]

run_comparison(sizes, distributions)