#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

from typing import (
    List
)


def binary_search_left(sorted_collection: List[int], item: int) -> int:
    """
    二分查找
    查找第一个值等于给定值的元素下标

    :param sorted_collection: 有序数组
    :param item: 要查找的数据项
    :return: index or -1
    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + ((right - left) >> 1)
        current_item = sorted_collection[midpoint]
        if current_item > item:
            right = midpoint - 1
        elif current_item < item:
            left = midpoint + 1
        else:
            if midpoint == 0 or sorted_collection[midpoint - 1] != item:
                return midpoint
            else:
                right = midpoint - 1
    return -1


def binary_search_right(sorted_collection: List[int], item: int) -> int:
    """
    二分查找
    查找最后一个值等于给定值元素下标

    :param sorted_collection: 有序数组
    :param item: 要查找的数据项
    :return: index or -1
    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + ((right - left) >> 1)
        current_item = sorted_collection[midpoint]
        if current_item > item:
            right = midpoint - 1
        elif current_item < item:
            left = midpoint + 1
        else:
            if midpoint == len(sorted_collection) - 1 or sorted_collection[midpoint + 1] != item:
                return midpoint
            else:
                left = midpoint + 1
    return -1


def binary_search_left_not_less(sorted_collection: List[int], item: int) -> int:
    """
    二分查找
    查找第一个大于等于给定值的元素

    :param sorted_collection: 有序数组
    :param item: 要查找的数据项
    :return: index or -1
    """
    left = 0
    right = len(sorted_collection) - 1
    while left <= right:
        midpoint = left + ((right - left) >> 1)
        current_item = sorted_collection[midpoint]
        if current_item < item:
            left = midpoint + 1
        else:
            if midpoint == 0 or sorted_collection[midpoint - 1] < item:
                return midpoint
            else:
                right = midpoint - 1
    return -1


def binary_search_right_not_greater(sorted_collection: List[int], item: int) -> int:
    """
    二分查找
    查找最后一个小于等于给定值的元素

    :param sorted_collection: 有序数组
    :param item: 要查找数据项
    :return: index or -1
    """
    left = 0
    right = len(sorted_collection) - 1
    while left <= right:
        midpoint = left + ((right - left) >> 1)
        current_item = sorted_collection[midpoint]
        if current_item > item:
            right = midpoint - 1
        else:
            if midpoint == len(sorted_collection) - 1 or sorted_collection[midpoint + 1] > item:
                return midpoint
            else:
                left = midpoint + 1
    return -1


if __name__ == "__main__":

    coll = [1, 2, 3, 3, 4, 5]
    print(binary_search_left(coll, 3))
    print(binary_search_right(coll, 3))
    print(binary_search_left_not_less(coll, 3))
    print(binary_search_right_not_greater(coll, 3))



