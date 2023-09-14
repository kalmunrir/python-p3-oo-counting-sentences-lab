#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value = ""):
    self.value = value

  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith('.')
    
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    if self.value.isspace() or self.value == '':
      return 0
    else:
      sentence_list = self.value
      sentence_list = sentence_list.replace('?', '.')
      sentence_list = sentence_list.replace('!', '.')
      sentence_list = sentence_list.split('.')
      sentence_list.sort()
      for i in range(sentence_list.count('')):
        sentence_list.remove('')
      return len(sentence_list)