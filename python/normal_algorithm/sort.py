#  -*- coding: utf-8 -*-
"""
Author: sanjin
basic sort algorithm
"""


def insert_sort(arr):
    """
    插入排序
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def select_sort(arr):
    """
    选择排序
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort(arr):
    """
    冒泡排序
    """
    size = len(arr)
    for i in range(size):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr, begin, end):
    """
    快速排序-递归实现
    """
    if begin >= end:
        return
    pivot = arr[begin]
    low, high = begin, end
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot
    quick_sort(arr, begin, low - 1)
    quick_sort(arr, low + 1, end)


def quick_sort_circle(arr):
    """
    快速排序-非递归实现
    """
    queue = [(0, len(arr) - 1)]
    while queue:
        begin, end = queue.pop()
        if begin >= end:
            continue
        low, high = begin, end
        pivot = arr[low]
        while low < high:
            while low < high and arr[high] >= pivot:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < pivot:
                low += 1
            arr[high] = arr[low]
        arr[low] = pivot
        queue.append((begin, low - 1))
        queue.append((low + 1, end))
    return arr


def better_select_sort(arr):
    """
    优化的选择排序
    """
    pass


if __name__ == '__main__':
    lst = [6, 2, 1, 3, 0, 5]
    print(quick_sort_circle(lst))
    # quick_sort(lst, 0, 5)
    # print(lst)
