#  -*- coding: utf-8 -*-
"""
Author: sanjin
classic dynamic programming algorithm
"""
from typing import List


# 爬楼梯
def climb_stairs(n: int) -> int:
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


# 打家劫舍
def rob1(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0 for _ in range(n + 1)]
    dp[1] = nums[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
    return dp[-1]


# 编辑距离
def edit_distance(word1: str, word2: str):
    l1, l2 = len(word1), len(word2)
    dp = [[0 for i in range(l1 + 1)] for j in range(l2 + 1)]
    for i in range(1, l1 + 1):
        dp[0][i] = i
    for j in range(1, l2 + 1):
        dp[j][0] = j
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1]
            else:
                dp[j][i] = min(dp[j - 1][i - 1], dp[j - 1][i], dp[j][i - 1]) + 1
    return dp[l2][l1]


# 最长递增子序列
def longest_increase_sublist(nums: List[int]):
    n = len(nums)
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        m = 0
        for j in range(i):
            if nums[j] < nums[i] and m < dp[j]:
                m = dp[j]
        dp[i] = m + 1
    return max(dp)


# 最长公共子序列
def longest_common_substr(s1: str, s2: str):
    l1, l2 = len(s1), len(s2)
    dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[l1][l2]


if __name__ == '__main__':
    # print(climb_stairs(3))
    # print(edit_distance("horse", "ros"))
    print(longest_increase_sublist([0, 1, 0, 3, 2, 3]))
    print(longest_common_substr("abcde", "ace"))
