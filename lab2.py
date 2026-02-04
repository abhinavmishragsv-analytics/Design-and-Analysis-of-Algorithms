import time
import random
import sys
import matplotlib.pyplot as plt
import pandas as pd
import math
sys.setrecursionlimit(20000)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

def merge_recursive(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_recursive(arr[:mid])
    right = merge_recursive(arr[mid:])
    return merge(left, right)

def merge_iterative(arr):
    n = len(arr)
    curr_size = 1
    while curr_size < n:
        for left in range(0, n, 2 * curr_size):
            mid = min(left + curr_size, n)
            right = min(left + 2 * curr_size, n)
            merged = merge(arr[left:mid], arr[mid:right])
            arr[left:left + len(merged)] = merged
        curr_size *= 2
    return arr

def quick_recursive(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_recursive(left) + middle + quick_recursive(right)

def partition(arr, l, h):
    i, x = (l - 1), arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quick_iterative(arr):
    size = len(arr)
    stack = [(0, size - 1)]
    while stack:
        l, h = stack.pop()
        if l < h:
            p = partition(arr, l, h)
            stack.append((l, p - 1))
            stack.append((p + 1, h))
    return arr

def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x: return mid
        elif arr[mid] > x: return binary_search_recursive(arr, low, mid - 1, x)
        else: return binary_search_recursive(arr, mid + 1, high, x)
    return -1

def binary_search_iterative(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x: low = mid + 1
        elif arr[mid] > x: high = mid - 1
        else: return mid
    return -1

sizes = [10, 100, 1000, 5000, 10000, 15000, 20000]

results = {
    "Size": sizes,
    "Merge Rec": [], "Merge Iter": [], 
    "Quick Rec": [], "Quick Iter": [],
    "BS Rec": [], "BS Iter": []
}

for s in sizes:
    arr_orig = [random.randint(0, 1000000) for _ in range(s)]
    
    for name, func in [("Merge Rec", merge_recursive), ("Merge Iter", merge_iterative),
                       ("Quick Rec", quick_recursive), ("Quick Iter", quick_iterative)]:
        arr_copy = arr_orig.copy()
        start = time.perf_counter()
        func(arr_copy)
        results[name].append(time.perf_counter() - start)
    
    sorted_arr = sorted(arr_orig)
    target = random.choice(sorted_arr)
    
    start = time.perf_counter()
    binary_search_recursive(sorted_arr, 0, len(sorted_arr)-1, target)
    results["BS Rec"].append(time.perf_counter() - start)
    
    start = time.perf_counter()
    binary_search_iterative(sorted_arr, target)
    results["BS Iter"].append(time.perf_counter() - start)

df = pd.DataFrame(results)
print("\n" + "="*80)
print(f"{'ALGORITHM BENCHMARK DATA':^80}")
print("="*80)
print(df.to_string(index=False))
print("="*80)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
for label in ["Merge Rec", "Merge Iter", "Quick Rec", "Quick Iter"]:
    plt.plot(sizes, results[label], label=label, marker='o')
plt.title("Sorting Time Complexity")
plt.xlabel("Array Size (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
for label in ["BS Rec", "BS Iter"]:
    plt.plot(sizes, results[label], label=label, marker='s')
plt.title("Binary Search Time Complexity")
plt.xlabel("Array Size (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()