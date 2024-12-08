#!/usr/bin/python3
# Created: Oct, 27, 2024 17:01:14 by Wataru Fukuda

import os
import watfio

class ConfigData():
  def __init__(self,mtype,filename=None):
    self.data_ = {}
    self.data_['integer'] = 4
    self.data_['float'] = 8
    self.heavy_ = {}
    self.fpath_ = {}
    self.original_dir_ = "."
    if(filename):
      self.original_dir_ = os.path.dirname(filename)
    self.type_ = mtype
    self.wfactory = watfio.WriterFactory()
    self.writer = self.wfactory.create(mtype)
  def get(self,dataname):
    return self.data_[dataname]
  def set(self,name,data):
    self.data_[name] = data
  def setHeavyData(self,name,data):
    self.heavy_[name] = data
  def setFilepath(self,datafile,filename):
    self.fpath_[datafile] = filename
  def setEndian(self,endian):
    if(endian =="little"):
      self.data_['endian'] = "<"
    else:
      self.data_['endian'] = ">"
  def writeAll(self,filename):
    self.writer = self.wfactory.create(self)
    self.writer.writeAll(filename)

