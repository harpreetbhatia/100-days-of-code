import pytest


def not_string(str):
  ## if (str.match('not')):
  if len(str) >= 3 and str[:3] == 'not':
    return str
  else:
    return 'not ' + str


def test_answer():
  assert not_string('candy') == 'not candy'
  assert not_string('x') == 'not x'
  assert not_string('not bad') == 'not bad'
  assert not_string('bad') == 'not bad'
  assert not_string('not') == 'not'
  assert not_string('is not') == 'not is not'
  assert not_string('no') == 'not no'

