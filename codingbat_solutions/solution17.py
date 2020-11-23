import pytest


def no_teen_sum(a, b, c):
  return fix_teen(a) + \
          fix_teen(b) + \
          fix_teen(c)
  
def fix_teen(n):
  if ((12 < n < 20) and (n != 15) and (n != 16)):
    return 0
  return n


def test_answer():
  assert no_teen_sum(1, 2, 3) == 6
  assert no_teen_sum(2, 13, 1) == 3
  assert no_teen_sum(2, 1, 14) == 3
  assert no_teen_sum(2, 1, 15) == 18
  assert no_teen_sum(2, 1, 16) == 19
  assert no_teen_sum(2, 1, 17) == 3
  assert no_teen_sum(17, 1, 2) == 3
  assert no_teen_sum(2, 15, 2) == 19
  assert no_teen_sum(16, 17, 18) == 16
  assert no_teen_sum(17, 18, 19) == 0
  assert no_teen_sum(15, 16, 1) == 32
  assert no_teen_sum(15, 15, 19) == 30
  assert no_teen_sum(15, 19, 16) == 31
  assert no_teen_sum(5, 17, 18) == 5
  assert no_teen_sum(17, 18, 16) == 16
  assert no_teen_sum(17, 19, 18) == 0

