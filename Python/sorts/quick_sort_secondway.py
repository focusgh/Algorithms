#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

from typing import List


def quick_sort(collection: List[int]) -> List[int]:
    """
    快速排序
    此方式，需要额外的空间开销来支持。
    """
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection.pop()
        greater, lesser = [], []
        for element in collection:
            if element >= pivot:
                greater.append(element)
            else:
                lesser.append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    test_list = [5, -1, 9, 3, 7]
    print(quick_sort(test_list))
