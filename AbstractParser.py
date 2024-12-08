#!/usr/bin/env python3
# Created: Dec, 04, 2024 11:08:17 by Wataru Fukuda

import abc

class AbstractParser(metaclass=abc.ABCMeta):
  def __init__(self,filename):
    self.filename_ = filename

