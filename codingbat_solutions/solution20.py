import pytest

def cat_dog(str):
  return (count(str, "cat") == count(str, "dog"))
  return False

def count(str, word):
  count = 0
  for i in range(len(str) - len(word) + 1):
    if (str[i:i+len(word)] == word):
      count += 1
  return count

def test_answer():
  assert cat_dog('catdog') == True
  assert cat_dog('catcat') == False
  assert cat_dog('1cat1cadodog') == True
  assert cat_dog('catxxdogxxxdog') == False
  assert cat_dog('catxdogxdogxcat') == True
  assert cat_dog('catxdogxdogxca') == False
  assert cat_dog('dogdogcat') == False
  assert cat_dog('dogogcat') == True
  assert cat_dog('dog') == False
  assert cat_dog('cat') == False
  assert cat_dog('ca') == True
  assert cat_dog('c') == True
  assert cat_dog('') == True

