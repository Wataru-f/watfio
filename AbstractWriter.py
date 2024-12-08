#!/usr/bin/env python3
# Created: Dec, 07, 2024 17:25:43 by Wataru Fukuda

from abc import ABCMeta,abstractmethod
import numpy
import os

class AbstractWriter(metaclass=ABCMeta):
  def __init__(self,config=None):
    if(config):
      self.config = config.data_
      self.heavy  = config.heavy_
      self.fpath = config.fpath_
      self.original_dir_ = config.original_dir_
    else:
      self.config = {}
      self.heavy  = {}
  def writeAll(self,filename):
    self.dir = os.path.dirname(filename)
    if(len(self.dir)>0 and not os.path.isdir(self.dir)):
      os.makedirs(self.dir)
    info = self.remakeInfo(self.config)
    self.writeInfo(filename,info)
    self.writeFileSection(filename,self.config)
  def remakeInfo(self,data):
    info = {}
    for sk in self.REMAKE_MAP:
      section = self.REMAKE_MAP[sk][0]
      key = self.REMAKE_MAP[sk][1]
      if(not info.get(section)):
        info[section] = {}
      value = data.get(sk)
      info[section][key] = value
    info["info"]["endian"] = "big" if info["info"].get("endian")==">" else "little"
    return info
  def writeFileSection(self,filename,data):
    typeTodtypeStr = { float : "f", int : "i" }
    typeToString = { float : "float", int : "integer" }
    file_info = {"file":{}}
    for key,d in self.DATA_TYPE.items():
      dataType = int
      if(key in self.heavy):
        da = self.heavy[key]
        if(numpy.dtype('f') < da.dtype):
          dataType = float
        dtype = data.get("endian") + typeTodtypeStr[dataType] + str(data.get(typeToString[dataType]))
        da = numpy.array(da,dtype=dtype)
        file=os.path.join(self.dir, d[0])
        da.tofile(open(file,"wb"))
        print (f"Wrote to {file}")
      if(d[3] or key in self.heavy):
        file_info["file"][key] = self.fpath.get(key,d[0])
    self.writeFileInfo(filename,file_info)

  @abstractmethod
  def writeInfo(self,filename,info):
    raise NotImplementedError
  @abstractmethod
  def writeFileInfo(self,filename,info):
    raise NotImplementedError

