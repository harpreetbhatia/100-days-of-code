import pytest

def big_diff(nums):
  if (len(nums) < 2):
    return 0

  smallest = nums[0]
  largest = nums[0]
  for num in nums:
    smallest = min(smallest, num)
    largest = max(largest, num)
  return (largest - smallest)
    
def test_answer():
  assert big_diff([10, 3, 5, 6]) == 7
  assert big_diff([7, 2, 10, 9]) == 8
  assert big_diff([2, 10, 7, 2]) == 8
  assert big_diff([2, 10]) == 8
  assert big_diff([10, 2]) == 8
  assert big_diff([10, 0]) == 10
  assert big_diff([2, 3]) == 1
  assert big_diff([2, 2]) == 0
  assert big_diff([2]) == 0
  assert big_diff([5, 1, 6, 1, 9, 9]) == 8
  assert big_diff([7, 6, 8, 5]) == 3
  assert big_diff([7, 7, 6, 8, 5, 5, 6]) == 3

