import random
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(200000)

def radix_sort_verbose(input_arr):
    arr = list(input_arr)
    print(f"\n--- RADIX SORT TRACE (Size {len(arr)}) ---")
    print(f"Initial Array: {arr}")
    
    max_val = max(arr)
    exp = 1
    step = 1
    
    while max_val // exp > 0:
        output = [0] * len(arr)
        count = [0] * 10
        
        for i in arr:
            index = (i // exp) % 10
            count[index] += 1
        
        print(f"\nStep {step} (Digit Place {exp}):")
        print(f"Auxiliary (Count) Array: {count}")
        
        for i in range(1, 10):
            count[i] += count[i - 1]
            
        for i in range(len(arr) - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            
        arr = list(output)
        print(f"Current Output Array: {arr}")
        exp *= 10
        step += 1
    return arr

def bucket_sort_verbose(input_arr):
    arr = list(input_arr)
    print(f"\n--- BUCKET SORT TRACE (Size {len(arr)}) ---")
    print(f"Initial Array: {[round(x, 3) for x in arr]}")
    
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    for j in arr:
        index_b = int(n * j)
        buckets[index_b].append(j)
    
    print("Auxiliary Structure (Buckets):")
    for i in range(n):
        print(f"  Bucket {i}: {[round(x, 3) for x in buckets[i]]}")
    
    output = []
    for i in range(n):
        buckets[i].sort() 
        output.extend(buckets[i])
        
    print(f"Final Output Array: {[round(x, 3) for x in output]}")
    return output

def radix_sort(arr):
    if not arr: return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        count = [0] * 10
        output = [0] * len(arr)
        for i in arr:
            count[(i // exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(len(arr) - 1, -1, -1):
            idx = (arr[i] // exp) % 10
            output[count[idx] - 1] = arr[i]
            count[idx] -= 1
        arr = output
        exp *= 10
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for j in arr:
        index_b = int(n * j)
        buckets[index_b].append(j)
    output = []
    for bucket in buckets:
        output.extend(sorted(bucket))
    return output

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

small_radix_data = [random.randint(100, 999) for _ in range(10)]
radix_sort_verbose(small_radix_data)

small_bucket_data = [random.random() for _ in range(10)]
bucket_sort_verbose(small_bucket_data)

sizes = [10, 100, 500, 1000, 10000] 
radix_times, insertion_times = [], []
bucket_times, quick_times = [], []


for n in sizes:
    int_data = [random.randint(0, 10000) for _ in range(n)]
    float_data = [random.random() for _ in range(n)]
    
    start = time.time()
    radix_sort(int_data.copy())
    radix_times.append(time.time() - start)
    
    start = time.time()
    insertion_sort(int_data.copy())
    insertion_times.append(time.time() - start)
    
    start = time.time()
    bucket_sort(float_data.copy())
    bucket_times.append(time.time() - start)
    
    start = time.time()
    quick_sort(float_data.copy())
    quick_times.append(time.time() - start)

plt.figure(figsize=(12, 5))
#  Radix vs Insertion
plt.subplot(1, 2, 1)
plt.plot(sizes, radix_times, label='Radix Sort (O(nk))', marker='o')
plt.plot(sizes, insertion_times, label='Insertion Sort (O(n²))', marker='s')
plt.title('Radix vs Insertion Sort')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
# Bucket vs Quick
plt.subplot(1, 2, 2)
plt.plot(sizes, bucket_times, label='Bucket Sort (O(n))', marker='o', color='green')
plt.plot(sizes, quick_times, label='Quicksort (O(n log n))', marker='s', color='red')
plt.title('Bucket vs Quicksort')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
