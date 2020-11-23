import pytest


def lone_sum(a, b, c):
  if (a == b and b == c):
    return 0
  if (a == b):
    return c
  if (b == c):
    return a
  if (c == a):
    return b
  return (a + b + c)

def test_answer():
  assert lone_sum(1, 2, 3) == 6
  assert lone_sum(3, 2, 3) == 2
  assert lone_sum(3, 3, 3) == 0
  assert lone_sum(9, 2, 2) == 9
  assert lone_sum(2, 2, 9) == 9
  assert lone_sum(2, 9, 2) == 9
  assert lone_sum(2, 9, 3) == 14
  assert lone_sum(4, 2, 3) == 9
  assert lone_sum(1, 3, 1) == 3

