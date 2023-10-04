"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


def median(nums):
    if len(nums) < 1:
        return

    if len(nums) % 2 == 0:
        num1 = nums[int(len(nums) / 2 - 1)]
        num2 = nums[int(len(nums) / 2)]
        return (num1 + num2) / 2
    else:
        return nums[int(len(nums) / 2)]


print(median(numbers))
