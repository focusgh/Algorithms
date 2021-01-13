#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

from typing import (
    List,
)


def _partition(collection, low, high):
    """
    原地分区函数
    """
    pivot = collection[high]
    # i 在 for 循环时，总是指向 “比较大区” 首元素下标
    i = low
    for j in range(low, high):
        if collection[j] < pivot:
            collection[i], collection[j] = collection[j], collection[i]
            i += 1
    collection[i], collection[high] = collection[high], collection[i]
    return i


def _quick_sort(collection: List[int], low: int, high: int) -> List[int]:
    """
    快速排序（实现）
    """

    if low >= high:
        return collection

    mid = _partition(collection, low, high)
    _quick_sort(collection, low, mid - 1)
    _quick_sort(collection, mid + 1, high)
    return collection


def quick_sort(collection: List[int]) -> List[int]:
    """
    快速排序

    不需要额外的空间开销，在待排序数组本身内部进行排序
    """
    return _quick_sort(collection, 0, len(collection) - 1)


if __name__ == "__main__":
    test_list = [5, 10, -1, 9, 3, 7]
    print(quick_sort(test_list))
