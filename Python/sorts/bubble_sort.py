#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

from typing import (
    List,
)


def bubble_sort(collection: List[int]) -> List[int]:
    """
    冒泡排序
    """
    length = len(collection)
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break
    return collection


if __name__ == "__main__":

    test_list = [1, 2, 5, 3, -1, 4, 5, 6]
    print(bubble_sort(test_list))
