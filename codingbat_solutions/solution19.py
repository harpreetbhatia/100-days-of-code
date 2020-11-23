import pytest

def count_hi(str):
count = 0
for i in range(len(str) - 1):
  if (str[i:i+2] == 'hi'):
    count += 1
return count

def test_answer():
  assert count_hi('abc hi ho') == 1
  assert count_hi('ABChi hi') == 2
  assert count_hi('hihi') == 2
  assert count_hi('hiHIhi') == 2
  assert count_hi('') == 0
  assert count_hi('h') == 0
  assert count_hi('hi') == 1
  assert count_hi('Hi is no HI on ahI') == 0
  assert count_hi('hiho not HOHIhi') == 2

