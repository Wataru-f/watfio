#!/usr/bin/env python3
# Created: Dec, 04, 2024 10:54:30 by Wataru Fukuda

import watfio

class ParserFactory:
  def __init__(self,filename=None):
    self.filename_ = filename
  def build(self):
    if(True):
      self.type_ = 'FEM'
    else:
      print("not supported yet")
      pass
    if(self.type_=='FEM'):
      return watfio.FEMParser(self.filename_)
    else:
      print("not supported yet")
      exit(1)

