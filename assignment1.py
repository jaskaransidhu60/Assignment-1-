# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: 10/21/2024
# Description: This code implements solutions to ten fundamental problems using StaticArray.
# The problems include min-max finding, FizzBuzz, reversing arrays, rotation,
# generating ranges, checking if sorted, finding mode, removing duplicates, count sorting, 
# and returning sorted squares. These functions are designed to work efficiently 
# with the provided StaticArray class.

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
    """Rotates elements of the StaticArray by the given steps."""
    n = arr.length()
    result = StaticArray(n)
    steps = steps % n  # Handle large step values
    for i in range(n):
        result.set((i + steps) % n, arr.get(i))
    return result


def sa_range(start: int, end: int) -> StaticArray:
    """Generates a StaticArray with consecutive integers from start to end."""
    size = abs(end - start) + 1
    result = StaticArray(size)
    step = 1 if start <= end else -1
    for i in range(size):
        result.set(i, start + i * step)
    return result


def is_sorted(arr: StaticArray) -> int:
    """Checks if the StaticArray is strictly sorted in ascending or descending order."""
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
    """Finds the mode (most frequent element) and its frequency."""
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
    """Removes duplicate elements from a sorted StaticArray."""
    if arr.length() == 0:
        return StaticArray(0)

    result = StaticArray(arr.length())
    result.set(0, arr.get(0))
    j = 1

    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            result.set(j, arr.get(i))
            j += 1

    final_result = StaticArray(j)
    for i in range(j):
        final_result.set(i, result.get(i))

    return final_result


def count_sort(arr: StaticArray) -> StaticArray:
    """Sorts the StaticArray using the count sort algorithm."""
    min_val = max_val = arr.get(0)

    for i in range(arr.length()):
        val = arr.get(i)
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    range_size = max_val - min_val + 1
    count = StaticArray(range_size)

    for i in range(range_size):
        count.set(i, 0)

    for i in range(arr.length()):
        count.set(arr.get(i) - min_val, count.get(arr.get(i) - min_val) + 1)

    result = StaticArray(arr.length())
    index = 0

    for i in range(range_size - 1, -1, -1):
        while count.get(i) > 0:
            result.set(index, i + min_val)
            index += 1
            count.set(i, count.get(i) - 1)

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
