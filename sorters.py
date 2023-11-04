import random
from consts import Data, DataPermutation

# Funktioner til at generere data

def generate_random_data(n : int) -> Data:
    """Genererer et datasæt med en længde n, med float-værdier i intervallet 0..1"""
    return [random.random() for _ in range(n)]

def generate_linear_data(n : int) -> Data:
    """Genererer et datsæt med en længde n, med float-værdier i intervallet 1/n..1"""
    data = [i / n for i in range(1, n + 1)]
    random.shuffle(data)
    return data

def generate_linear_ints(n : int) -> Data:
    """Genererer et datsæt med en længde n, med int-værdier i intervallet 1..n"""
    data = list(range(0, n + 1))
    random.shuffle(data)
    return data

# Sorterings-algoritmer

def bubble_sort(data : Data) -> DataPermutation:
    """Implementation af bubble-sort algoritmen, med tidskompleksiteten O(n²)"""
    data_copy = [n for n in data]
    data_len = len(data)

    for i in range(data_len):
        changes_made = False

        for j in range(data_len - i):
            if j == data_len - 1: continue

            if data_copy[j] > data_copy[j + 1]:
                data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
                changes_made = True
                yield (data_copy, [j, j + 1])
            else:
                yield (data_copy, [j, j])
        
        if not changes_made:
            break

def selection_sort(data : Data) -> DataPermutation:
    """Implementation af selection-sort algoritmen, med tidskompleksiteten O(n²)"""
    data_copy = [n for n in data]
    data_len = len(data)

    for i in range(data_len):

        last_index = data_len - i - 1
        max_index = last_index
        
        for j in range(data_len - i):
            if (data_copy[j] > data_copy[max_index]): max_index = j
        
        data_copy[last_index], data_copy[max_index] = data_copy[max_index], data_copy[last_index]

        yield (data_copy, [last_index, max_index])

def insertion_sort(data : Data) -> DataPermutation:
    """Implementation af insertion-sort algoritmen, med tidskompleksiteten O(n²)"""
    data_copy = [n for n in data]
    data_len = len(data)

    for i in range(1, data_len):
        val = data_copy[i]
        retrace_index = i - 1

        while retrace_index >= 0 and val < data_copy[retrace_index]:
            data_copy[retrace_index + 1] = data_copy[retrace_index]
            retrace_index -= 1

        data_copy[retrace_index + 1] = val

        yield (data_copy, [i, retrace_index])

def merge_sort(data : Data, modifiable_data : Data = [], start : int = 0, stop : int = -1) -> DataPermutation:
    """Implementation af merge-sort algoritmen, med tidskompleksiteten O(n log(n))"""
    if stop == -1:
        stop = len(data) - 1
        modifiable_data = [n for n in data]

    if start < stop:

        divide = start + (stop - start) // 2
 
        yield from merge_sort([], modifiable_data, start, divide)
        yield from merge_sort([], modifiable_data, divide + 1, stop)

        i, j = start, divide + 1
        auxiliary = [None for _ in range(stop - start + 1)]

        for k in range(stop - start + 1):
            if i > divide:
                auxiliary[k:] = modifiable_data[j:stop + 1]
                break
            elif j > stop:
                auxiliary[k:] = modifiable_data[i:divide + 1]
                break

            if modifiable_data[i] < modifiable_data[j]:
                auxiliary[k] = modifiable_data[i]
                i += 1
            else:
                auxiliary[k] = modifiable_data[j]
                j += 1
            
            yield (modifiable_data, [i, j])

        modifiable_data[start:stop + 1] = auxiliary
        yield (modifiable_data, [0])

def shell_sort(data : Data) -> DataPermutation:
    """Implementation af merge-sort algoritmen, med tidskompleksiteten O(n log(n)²)"""
    data_copy = [n for n in data]
    data_len = len(data)
    gap = data_len // 2

    while gap > 0:
        for i in range(gap, data_len):
            j = i - gap

            while j >= 0:
                if data_copy[j] > data_copy[j + gap]:
                    data_copy[j], data_copy[j + gap] = data_copy[j + gap], data_copy[j]
                    yield (data_copy, [j, j + gap])
                else:
                    break
                    
                j -= gap

        gap //= 2
