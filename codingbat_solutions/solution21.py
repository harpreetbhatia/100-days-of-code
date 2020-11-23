import pytest

def count_code(str):
  count = 0
  for i in range(len(str) - 3):
    if (str[i:i+2] == 'co' and str[i+3] == 'e'):
      count += 1
  return count

def test_answer():
  assert count_code('aaacodebbb') == 1
  assert count_code('codexxcode') == 2
  assert count_code('cozexxcope') == 2
  assert count_code('cozfxxcope') == 1
  assert count_code('xxcozeyycop') == 1
  assert count_code('cozcop') == 0
  assert count_code('abcxyz') == 0
  assert count_code('code') == 1
  assert count_code('ode') == 0
  assert count_code('c') == 0
  assert count_code('') == 0
  assert count_code('AAcodeBBcoleCCccoreDD') == 3
  assert count_code('AAcodeBBcoleCCccorfDD') == 2
  assert count_code('coAcodeBcoleccoreDD') == 3

