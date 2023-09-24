import random
from consts import Data, DataHighlight

# Data generators

def generate_data(n : int) -> Data:
    """Generates an array with length 'n' with floats in the range 0..1"""
    return [random.random() for _ in range(n)]

def generate_linear_data(n : int) -> Data:
    """TODO:"""
    data = [i / n for i in range(1, n + 1)]
    random.shuffle(data)
    return data

# Sorting algorithms

def bubble_sort(data : Data) -> DataHighlight:
    """Implementation of the bubble sort algorithm, with yields a copy of the sorted data every step TODO:FIXME:"""
    data_copy = [n for n in data]
    data_len = len(data)

    for i in range(data_len):
        changes_made = False

        for j in range(data_len - i):
            if j == data_len - 1: continue

            if data_copy[j] > data_copy[j + 1]:
                data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
                changes_made = True
        
            # yield (data_copy, [j, j + 1])
            yield (data_copy, [j, j + 1, j + 2])
        
        if not changes_made:
            break

def selection_sort(data : Data) -> DataHighlight:
    data_copy = [n for n in data]
    data_len = len(data)

    for i in range(data_len):

        last_index = data_len - i - 1
        max_index = last_index
        
        for j in range(data_len - i):
            if (data_copy[j] > data_copy[max_index]): max_index = j
        
        data_copy[last_index], data_copy[max_index] = data_copy[max_index], data_copy[last_index]

        yield (data_copy, [last_index, max_index])

def insertion_sort(data : Data) -> DataHighlight:
    data_copy = [n for n in data]
    data_len = len(data)

    for i in range(1, data_len):

        val = data_copy[i]
        retrace_index = i - 1

        while retrace_index >= 0 and val < data_copy[retrace_index]:
            data_copy[retrace_index + 1] = data_copy[retrace_index]
            retrace_index -= 1 #FIXME:TODO:

        data_copy[retrace_index + 1] = val

        yield (data_copy, [i, retrace_index])

def merge_sort(data : Data) -> DataHighlight:
    pass

def stalin_sort(data : Data) -> DataHighlight:
    data_copy = [n for n in data]

    index = 1

    while index < len(data_copy):
        if data_copy[index - 1] > data_copy[index]:
            data_copy.pop(index)
        else:
            index += 1
        yield (data_copy, [index - 1, index])

    # for i in range(1, data_len):
    #     if data_copy[i - 1] > data_copy[i]:
    #         data_copy.pop(i - offset)
    #         offset += 1
    #     yield data_copy

def shell_sort(data : Data) -> DataHighlight:
    gap = len(data) // 2

    while gap > 0:
        j = gap

        while j < len(data):
            i = j - gap
              
            while i >= 0:
                if data[i+gap]>data[i]:
                    break

                else:
                    data[i+gap],data[i]=data[i],data[i+gap]
                    yield (data, [i, j, gap])
  
                i = i - gap
            
            j += 1
        
        gap = gap // 2




def merge(arr, start, divide, stop):
    first_length = divide - start + 1
    second_length = stop - divide
 
    # create temp arrays
    first_half = [0] * first_length
    second_half = [0] * second_length
 
    # Copy data to temp arrays L[] and R[]
    for i in range(first_length):
        first_half[i] = arr[start + i]
 
    for j in range(second_length):
        second_half[j] = arr[divide + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = start # Initial index of merged subarray

    while i < first_length and j < second_length:
        if first_half[i] <= second_half[j]:
            arr[k] = first_half[i]
            i += 1
        else:
            arr[k] = second_half[j]
            j += 1
        k += 1

        yield (arr, [k - 1])
    
    # Copy the remaining elements of L[], if there
    # are any
    while i < first_length:
        arr[k] = first_half[i]
        i += 1
        k += 1

        yield (arr, [0])
    
    # Copy the remaining elements of R[], if there
    # are any
    while j < second_length:
        arr[k] = second_half[j]
        j += 1
        k += 1

        yield (arr, [0])
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, start = 0, stop = -1):
    if stop == -1: stop = len(arr) - 1

    if start < stop:

        divide = start + (stop - start) // 2
 
        yield from mergeSort(arr, start, divide)
        yield from mergeSort(arr, divide + 1, stop)
        yield from merge(arr, start, divide, stop)
