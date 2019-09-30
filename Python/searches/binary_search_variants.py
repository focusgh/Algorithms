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
        midpoint = (left + right) // 2
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
        midpoint = (left + right) // 2
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