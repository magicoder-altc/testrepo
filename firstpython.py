import random
from typing import List


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    # Given the problem guarantees exactly one solution, we shouldn't get here.
    raise ValueError("No valid two-sum solution found.")


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    my_list.insert(2, 6)
    print(my_list)
