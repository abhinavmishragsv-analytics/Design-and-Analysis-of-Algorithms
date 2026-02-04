import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    passes = comparisons = swaps = 0

    for i in range(n - 1):
        min_index = i
        passes += 1
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return passes, comparisons, swaps


def bubble_sort(arr):
    n = len(arr)
    passes = comparisons = swaps = 0

    for i in range(n - 1):
        passes += 1
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return passes, comparisons, swaps


def insertion_sort(arr):
    n = len(arr)
    passes = comparisons = swaps = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        passes += 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1

        arr[j + 1] = key

    return passes, comparisons, swaps


sizes = [10, 15, 25, 50, 100, 250, 500, 1000, 2000]

results = {
    "Selection": {"passes": [], "comparisons": [], "swaps": [], "time": []},
    "Bubble": {"passes": [], "comparisons": [], "swaps": [], "time": []},
    "Insertion": {"passes": [], "comparisons": [], "swaps": [], "time": []},
}

for size in sizes:
    original = [random.randint(0, 10000) for _ in range(size)]

    for name, sort_func in [
        ("Selection", selection_sort),
        ("Bubble", bubble_sort),
        ("Insertion", insertion_sort)
    ]:
        arr = original.copy()
        start = time.time()
        p, c, s = sort_func(arr)
        end = time.time()

        results[name]["passes"].append(p)
        results[name]["comparisons"].append(c)
        results[name]["swaps"].append(s)
        results[name]["time"].append(end - start)



plt.figure(figsize=(14, 10))


plt.subplot(2, 2, 1)
for algo in results:
    plt.plot(sizes, results[algo]["passes"], label=algo)
plt.xlabel("Array Size")
plt.ylabel("Number of Passes")
plt.title("Passes vs Array Size")
plt.legend()
plt.grid()


plt.subplot(2, 2, 2)
for algo in results:
    plt.plot(sizes, results[algo]["comparisons"], label=algo)
plt.xlabel("Array Size")
plt.ylabel("Number of Comparisons")
plt.title("Comparisons vs Array Size")
plt.legend()
plt.grid()


plt.subplot(2, 2, 3)
for algo in results:
    plt.plot(sizes, results[algo]["swaps"], label=algo)
plt.xlabel("Array Size")
plt.ylabel("Number of Swaps")
plt.title("Swaps vs Array Size")
plt.legend()
plt.grid()


plt.subplot(2, 2, 4)
for algo in results:
    plt.plot(sizes, results[algo]["time"], label=algo)
plt.xlabel("Array Size")
plt.ylabel("Time Taken (seconds)")
plt.title("Time vs Array Size")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
