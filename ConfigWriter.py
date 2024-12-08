#!/usr/bin/env python3
# Created: Dec, 07, 2024 17:22:21 by Wataru Fukuda

from watfio.AbstractWriter import AbstractWriter
import numpy

class ConfigWriter(AbstractWriter):
  def writeInfo(self,filename,info):
    fwrite = open(filename,"w")
    for section in info:
      print(f"[{section}]",file=fwrite)
      for key in info[section]:
        value = info[section][key]
        if(isinstance(value,list) or type(value)==numpy.ndarray) :
          for v in value:
            print(f"{key} = {v}",file=fwrite)
        else:
          value = str(value)
          print(f"{key} = {value}",file=fwrite)
    fwrite.close()
  def writeFileInfo(self,filename,info):
    fadd = open(filename,"a")
    for section in info:
      print(f"[{section}]",file=fadd)
      for key in info[section]:
        value = info[section][key]
        print(f"{key} = {value}",file=fadd)
    fadd.close()

