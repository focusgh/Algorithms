#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'


class Solution:

    def is_valid(self, s: str) -> bool:

        # 长度为奇数直接返回 False
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []
        for i in s:
            if i in pairs:
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return not stack


if __name__ == "__main__":
    input_str = "{}({()})"
    res = Solution().is_valid(input_str)
    print(res)
