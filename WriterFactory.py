#!/usr/bin/python3
# Created: Oct, 27, 2024 17:14:45 by Wataru Fukuda

import watfio

class WriterFactory:
  def __init__(self):
    self.cwf = ConfigWriterFactory()
  def create(self, Type):
    return self.cwf.create(Type)

class ConfigWriterFactory:
  def __init__(self):
    pass
  def create(self, Type):
    if isinstance(Type, str):
      mesh_type = Type
      default_data = None
    elif isinstance(Type, watfio.ConfigData):
      mesh_type = Type.type_
      default_data = Type
    if(mesh_type=='FEM'):
      return watfio.FEMConfigWriter(default_data)
    else:
      print("Not supported yet")
      exit(1)

