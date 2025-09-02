from typing import Callable
import time

def time_algorithm(algo: Callable[[], [list[int]]], arr: list[int]) -> float:
    start = time.time()
    algo(arr.copy())
    return time.time() - start


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
    

if __name__ == '__main__':
    import random
    sizes = [100, 500, 1000, 5000]
    size = random.choice(sizes)
    arr = [random.randint(0, size) for _ in range(size)]
    
    print("Before WIP merge Sort: ", arr)
    sorted_arr = merge_sort(arr)
    print("After merge sort: ", sorted_arr)