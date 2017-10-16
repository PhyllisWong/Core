import random
"""In class challenges for Core - Pair-Programming."""


def dice_roller(roll):
    """
    Take in a String, nds where n = num of dice, s = num of sides.
    Returns the total of the rolls.
    """
    if (type(roll) != str):
        return

    total = 0

    components = roll.split("d")
    num_rolls = int(components[0])
    num_sides = int(components[1])

    for die_roll in range(0, num_rolls):
        toss = random.randint(1, num_sides)
        total += toss

    return total


if __name__ == '__main__':
    """Allow for testing from the console. Input arguments after file name."""
    from sys import argv

    roll = argv[1]
    print(dice_roller(roll))


"""Sum Problem"""
"""
Given an array of integers, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2. Please note that your
returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9 Output: index1=0, index2=1

Your twoSum method should take two inputs, first is an array of integers, and
a second is the target to sum to:

twoSum([2, 7, 11, 15], 9)
If you are done with this problem, figure out and write down the Big-O of your
twoSum implementation. Try to solve it in O(N) time and space.
"""


def twoSum(nums, target):
    """Find the indices of 2 numbers in the array, that sum to target."""
    i = 0
    j = 0
    while nums[i] + nums[j] != target:
        if j < len(nums) - 1:
            j += 1
        else:
            i += 1
            j += 1
    print([i, j])
    return [i, j]


twoSum([3, 7, 4, 11, 13], 16)
