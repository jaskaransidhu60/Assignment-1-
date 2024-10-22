from static_array import StaticArray

def min_max(arr: StaticArray) -> tuple[int, int]:
    """Finds the minimum and maximum values in a StaticArray."""
    min_val = arr.get(0)
    max_val = arr.get(0)
    for i in range(arr.length()):
        val = arr.get(i)
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val
    return min_val, max_val

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """Replaces integers divisible by 3 and/or 5 with strings."""
    result = StaticArray(arr.length())
    for i in range(arr.length()):
        val = arr.get(i)
        if val % 3 == 0 and val % 5 == 0:
            result.set(i, 'fizzbuzz')
        elif val % 3 == 0:
            result.set(i, 'fizz')
        elif val % 5 == 0:
            result.set(i, 'buzz')
        else:
            result.set(i, val)
    return result

def reverse(arr: StaticArray) -> None:
    """Reverses the StaticArray in place."""
    left, right = 0, arr.length() - 1
    while left < right:
        temp = arr.get(left)
        arr.set(left, arr.get(right))
        arr.set(right, temp)
        left += 1
        right -= 1

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """Rotates the StaticArray by the given number of steps."""
    n = arr.length()
    result = StaticArray(n)
    steps = steps % n  # Handle large steps
    for i in range(n):
        result.set((i + steps) % n, arr.get(i))
    return result

def sa_range(start: int, end: int) -> StaticArray:
    """Returns a StaticArray with consecutive integers from start to end."""
    size = abs(end - start) + 1
    result = StaticArray(size)
    step = 1 if start <= end else -1
    for i in range(size):
        result.set(i, start + i * step)
    return result

def is_sorted(arr: StaticArray) -> int:
    """Checks if the StaticArray is sorted."""
    ascending = True
    descending = True
    for i in range(1, arr.length()):
        if arr.get(i) < arr.get(i - 1):
            ascending = False
        if arr.get(i) > arr.get(i - 1):
            descending = False
    if ascending:
        return 1
    elif descending:
        return -1
    else:
        return 0

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """Finds the mode of the StaticArray."""
    mode = arr.get(0)
    max_count = 1
    current_count = 1
    for i in range(1, arr.length()):
        if arr.get(i) == arr.get(i - 1):
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            max_count = current_count
            mode = arr.get(i)
    return mode, max_count

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """Removes duplicates from a sorted StaticArray."""
    if arr.length() == 0:
        return StaticArray(0)
    result = StaticArray(arr.length())
    result.set(0, arr.get(0))
    j = 1
    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            result.set(j, arr.get(i))
            j += 1
    return StaticArray(j)  # Trim to the correct size

def count_sort(arr: StaticArray) -> StaticArray:
    """Sorts the StaticArray using counting sort."""
    min_val = min_max(arr)[0]
    max_val = min_max(arr)[1]
    count = [0] * (max_val - min_val + 1)
    for i in range(arr.length()):
        count[arr.get(i) - min_val] += 1
    result = StaticArray(arr.length())
    index = 0
    for i, c in enumerate(count):
        while c > 0:
            result.set(index, i + min_val)
            index += 1
            c -= 1
    return result

def sorted_squares(arr: StaticArray) -> StaticArray:
    """Returns a StaticArray with squares of elements sorted."""
    n = arr.length()
    result = StaticArray(n)
    left, right, index = 0, n - 1, n - 1
    while left <= right:
        left_square = arr.get(left) ** 2
        right_square = arr.get(right) ** 2
        if left_square > right_square:
            result.set(index, left_square)
            left += 1
        else:
            result.set(index, right_square)
            right -= 1
        index -= 1
    return result
