# Given an expression string, write a python program to find
# whether a given string has balanced parentheses or not.

def balanced(p_set):
    count = 0
    for p in p_set:
        if p == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0

# print(balanced('()()()()((()))()(()())'))
# print(balanced('((()))()()()()((()))){{{{{'))
# print(balanced('()))()()('))

# Given an expression string, write a python program to find whether a
# given string has balanced grouping symbols or not.

# def balanced_brackets(string):
#     bracket_dict = {'(': ')', '[': ']', '{': '}'}
#     stack = []
#
#     for s in string:
#         if s in bracket_dict.keys():
#             stack.append(bracket_dict[s])
#         elif s in bracket_dict.values():
#             if stack == [] or s != stack.pop():
#                 return False
#     return stack == []
#
#     # brackets = ['()', '[]', '{}']
#     # while [x in string for x in brackets] != []:
#     #     for b in brackets:
#     #         if b in string:
#     #             string.replace(b, '')
#     # return string == []
#
#
# # print(balanced_brackets('()()()()((()))()(()())'))
# print(balanced_brackets('((()))()()()()((()))){{{{{'))

"""
fib(0) = 0
fib(1) = 1
fib(2) = 1

define function fib(n) that returns the nth Fibonacci number.
"""

def fib(n):
    a = 0
    b = 1
    for _ in range(n-1):
        c = a + b
        a = b
        b = c
    return c

# print(fib(10))

    # fib_list = [0, 1] # 0,1,1,2,3,5,8,13,21,34,55
    # for i in range(2, n+1):
    #     fib_list.append(fib_list[i-2] + fib_list[i-1])
    # return fib_list[n]

# print(fib(8))

def recursive_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fib(n-1) + recursive_fib(n-2)

# print(recursive_fib(10))

# ----------------------------------------------

from collections import defaultdict

# class Solution(object):
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    store = defaultdict(list)
    for i, num in enumerate(nums):
        diff = target - num
        if diff in store.keys():
            return [store[diff], i]
        else:
            store[num] = i

print(twoSum([3,2,4], 6))

