import pytest

def end_other(a, b):
  str_a = a.lower()
  str_b = b.lower()
  return (str_a.endswith(str_b) or str_b.endswith(str_a))


def test_answer():
  assert end_other('Hiabc', 'abc') == True
  assert end_other('AbC', 'HiaBc') == True
  assert end_other('abc', 'abXabc') == True
  assert end_other('Hiabc', 'abcd') == False
  assert end_other('Hiabc', 'bc') == True
  assert end_other('Hiabcx', 'bc') == False
  assert end_other('abc', 'abc') == True
  assert end_other('xyz', '12xyz') == True
  assert end_other('yz', '12xz') == False
  assert end_other('Z', '12xz') == True
  assert end_other('12', '12') == True
  assert end_other('abcXYZ', 'abcDEF') == False
  assert end_other('ab', 'ab12') == False
  assert end_other('ab', '12ab') == True

