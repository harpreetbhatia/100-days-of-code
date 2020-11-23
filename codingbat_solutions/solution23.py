import pytest

def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if (nums[i] % 2 == 0):
      count += 1
  return count


def count_evens(nums):
  count = 0
  for num in nums:
    if (num % 2 == 0):
      count += 1
  return count

def test_answer():
  assert count_evens([2, 1, 2, 3, 4]) == 3
  assert count_evens([2, 2, 0]) == 3
  assert count_evens([1, 3, 5]) == 0
  assert count_evens([]) == 0
  assert count_evens([11, 9, 0, 1]) == 1
  assert count_evens([2, 11, 9, 0]) == 2
  assert count_evens([2]) == 1
  assert count_evens([2, 5, 12]) == 2

