# Heapsort, Priority Queue, and Sorting Algorithm Comparison

This assignment implements Heapsort, a Priority Queue using a binary max-heap, and provides an empirical comparison of Heapsort with other popular sorting algorithms.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Heapsort Implementation](#heapsort-implementation)
4. [Priority Queue Implementation](#priority-queue-implementation)
5. [Empirical Comparison of Sorting Algorithms](#empirical-comparison-of-sorting-algorithms)
6. [Performance Analysis](#performance-analysis)
7. [Findings and Conclusions](#findings-and-conclusions)

## Installation

This assignment requires Python 3.6 or higher. No additional libraries are needed.

To get started, clone this repository:

## Usage

To run the Heapsort implementation:
To run the Priority Queue examples:
To run the sorting algorithm comparison:

## Heapsort Implementation

The Heapsort implementation includes:

- `heapify`: Maintains the heap property for a subtree rooted at a given index.
- `build_heap`: Constructs a max-heap from an unsorted array.
- `heapsort`: Sorts an array using the Heapsort algorithm.

## Priority Queue Implementation

The Priority Queue is implemented as a binary max-heap and includes:

- `insert`: Adds a new element to the queue.
- `extract_max`: Removes and returns the highest priority element.
- `increase_key`: Increases the priority of a given element.
- `is_empty`: Checks if the queue is empty.

## Empirical Comparison of Sorting Algorithms

This project includes an empirical comparison of Heapsort with Quicksort and Merge Sort.

### Comparison Details

- **Algorithms compared**: Heapsort, Quicksort, Merge Sort
- **Input sizes**: 1000, 10000, 100000 elements
- **Input distributions**: Sorted, Reverse-sorted, Random

### Running the Comparison

To run the comparison:

1. Execute the script:
2. Results will be exported to "output.txt" in the same directory.

### Interpreting the Results

The "output.txt" file contains running times of each algorithm for different input sizes and distributions. Key points to observe:

- Relative performance of Heapsort compared to Quicksort and Merge Sort.
- Impact of input distributions on each algorithm's performance.
- Scaling of running times with increasing input size.

## Performance Analysis

### Heapsort
- Time Complexity: O(n log n) for all cases
- Space Complexity: O(1) (in-place sorting)

### Priority Queue
- Insert: O(log n)
- Extract Max: O(log n)
- Increase Key: O(n) (can be optimized to O(log n))
- Is Empty: O(1)

Where n is the number of elements in the heap/queue.

## Findings and Conclusions

1. Heapsort provides consistent O(n log n) performance across all input distributions.
2. The Priority Queue implementation demonstrates efficiency in various applications like task scheduling and data processing.
3. Empirical comparison reveals nuances in performance between Heapsort, Quicksort, and Merge Sort under different conditions.
4. Heapsort's in-place sorting capability makes it memory-efficient compared to Merge Sort.
5. While theoretically similar in time complexity, practical performance can vary due to factors like cache efficiency and specific input characteristics.
6. The Priority Queue shows versatility in handling dynamic data with changing priorities.
7. Future work could focus on optimizing the increase_key operation in the Priority Queue and exploring hybrid sorting algorithms.

This assignment demonstrates the effectiveness of heap-based data structures and algorithms in sorting and priority-based data management, providing insights into their practical performance characteristics.