from typing import Callable
import time
import click
import random

def time_algorithm(algo: Callable[[], [list[int]]], arr: list[int]) -> float:
    start = time.perf_counter()
    algo(arr.copy())
    return time.perf_counter() - start


def selection_sort(arr: list[int]) -> list[int]:
    l = len(arr)
    for i in range(l - 1):
        min_idx = i
        
        for j in range(i + 1, l):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr
        


def merge(left: list[int], right: list[int]) -> list[int]:
    merged_arr = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])
    
    return merged_arr
            

def merge_sort(arr: list[int]) -> list[int]:
    # TODO: Implement
    if len(arr) == 0 or len(arr) == 1:
        return arr
    
    if len(arr) == 2:
        # do sorting
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    
    mid = len(arr) // 2
    
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
    
@click.command()
@click.option("--seed", default=100, help="seed for algorithms. Default is 100")
def main(seed: int):
    print("Seed set to: ", seed)
    arr = [random.randint(0, seed) for _ in range(seed)]
    time.sleep(1)
    print("Running Mergesort...")
    timed_ms = time_algorithm(merge_sort, arr)
    time.sleep(1)
    print(f"Mergesort took: {timed_ms} seconds")
    print("Running Selection Sort...")
    timed_ss = time_algorithm(selection_sort, arr)
    print(f"Selection sort took: {timed_ss} seconds")
    time.sleep(1)
    print(f"\n\nFinal Times: \n Mergesort: {timed_ms} seconds\n Selection sort: {timed_ss} seconds")

if __name__ == '__main__':
    main()