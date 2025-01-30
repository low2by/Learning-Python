

# Common Big-O Complexities
# O(1) - Constant Time: The execution time does not change regardless of input size.
# Example: Accessing an element in an array by index.
def get_first_element(arr):
    return arr[0]  # O(1) - Always executes once

# O(log n) - Logarithmic Time: The execution time increases logarithmically as the input size grows.
# Example: Binary search.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # O(log n) - Reduces problem size by half each iteration
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # O(1) - Single return operation

# O(n) - Linear Time: The execution time grows proportionally with the input size.
# Example: Looping through an array.
def print_all_elements(arr):
    for element in arr:  # O(n) - Iterates through all elements once
        print(element)

# O(n log n) - Linearithmic Time: Slightly worse than linear but better than quadratic.
# Example: Efficient sorting algorithms like Merge Sort or Quick Sort.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # O(1) - Base case

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # O(log n) - Recursively divide into halves
    right = merge_sort(arr[mid:])  # O(log n) - Recursively divide into halves
    
    return merge(left, right)  # O(n) - Merging step

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):  # O(n) - Combining sorted parts
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # O(n) - Convert list into a heap
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]  # O(n log n) - Extract elements
    return sorted_arr

# O(n²) - Quadratic Time: Execution time grows proportionally to the square of input size.
# Example: Nested loops, like checking all pairs in a list.
def print_pairs(arr):
    for i in range(len(arr)):  # O(n) - Outer loop
        for j in range(len(arr)):  # O(n) - Inner loop (nested)
            print(arr[i], arr[j])  # Runs O(n²) times

# O(2ⁿ) - Exponential Time: Execution time doubles with each additional input.
# Example: Recursive Fibonacci calculation.
def fibonacci(n):
    if n <= 1:
        return n  # O(1) - Base case
    return fibonacci(n - 1) + fibonacci(n - 2)  # O(2ⁿ) - Two recursive calls per step

# O(n!) - Factorial Time: Execution time grows extremely fast, often infeasible for large inputs.
# Example: Solving the Traveling Salesman Problem via brute force.
from itertools import permutations

def all_permutations(arr):
    perms = permutations(arr)  # O(n!) - Generates all possible orderings
    for perm in perms:  # O(n!) - Iterates through all permutations
        print(perm)

def main():
    print("hello world")

if __name__ == "__main__":
    main()
