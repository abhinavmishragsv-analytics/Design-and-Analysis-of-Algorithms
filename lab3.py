def counting_sort_verbose(arr):
    print("Input Array:", arr)

    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    print("\nInitial Count Array:", count)
    print("Initial Output Array:", output)

    # Step 1: Count occurrences
    print("\n--- Counting Occurrences ---")
    for num in arr:
        count[num] += 1
        print(f"After processing {num}: Count = {count}")

    # Step 2: Cumulative count
    print("\n--- Cumulative Count ---")
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        print(f"Count[{i}] updated: {count}")

    # Step 3: Build output array
    print("\n--- Building Output Array ---")
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
        print(f"Placed {num}: Output = {output}, Count = {count}")

    print("\nFinal Sorted Array:", output)
    return output


# Execute for array size 10
import random
arr_10 = [random.randint(0, 9) for _ in range(10)]
counting_sort_verbose(arr_10)
import random
import time
import matplotlib.pyplot as plt

# ---------- Sorting Algorithms ----------
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    return output

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# ---------- Experiment ----------
sizes = [10,100,1000,10000, 100000, 1000000]

count_t, insert_t, bubble_t, select_t = [], [], [], []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]

    start = time.perf_counter()
    counting_sort(arr.copy())
    count_t.append(time.perf_counter() - start)

    start = time.perf_counter()
    insertion_sort(arr.copy())
    insert_t.append(time.perf_counter() - start)

    start = time.perf_counter()
    bubble_sort(arr.copy())
    bubble_t.append(time.perf_counter() - start)

    start = time.perf_counter()
    selection_sort(arr.copy())
    select_t.append(time.perf_counter() - start)

# ---------- Graph ----------
plt.figure(figsize=(10,6))
plt.plot(sizes, count_t, label="Counting Sort")
plt.plot(sizes, insert_t, label="Insertion Sort")
plt.plot(sizes, bubble_t, label="Bubble Sort")
plt.plot(sizes, select_t, label="Selection Sort")

plt.xlabel("Array Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Time Comparison")
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.show()
