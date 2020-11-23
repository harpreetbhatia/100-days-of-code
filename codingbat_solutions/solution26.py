import pytest


def centered_average(nums):
  sum = 0
  for num in nums:
    sum += num
  sum -= (smallest(nums) + largest(nums))
  avg = sum / (len(nums) - 2)
  return avg
  

def smallest(nums):
  smallest = nums[0]
  for num in nums:
    smallest = min(smallest, num)
  return smallest

def largest(nums):
  largest = nums[0]
  for num in nums:
    largest = max(largest, num)
  return largest

def test_answer():
  assert centered_average([1, 2, 3, 4, 100]) == 3
  assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
  assert centered_average([-10, -4, -2, -4, -2, 0]) == -3
  assert centered_average([5, 3, 4, 6, 2]) == 4
  assert centered_average([5, 3, 4, 0, 100]) == 4
  assert centered_average([100, 0, 5, 3, 4]) == 4
  assert centered_average([4, 0, 100]) == 4
  assert centered_average([0, 2, 3, 4, 100]) == 3
  assert centered_average([1, 1, 100]) == 1
  assert centered_average([7, 7, 7]) == 7
  assert centered_average([1, 7, 8]) == 7
  assert centered_average([1, 1, 99, 99]) == 50
  assert centered_average([1000, 0, 1, 99]) == 50
  assert centered_average([4, 4, 4, 4, 5]) == 4
  assert centered_average([4, 4, 4, 1, 5]) == 4
  assert centered_average([6, 4, 8, 12, 3]) == 6

