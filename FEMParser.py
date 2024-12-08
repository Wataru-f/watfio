#!/usr/bin/env python3
# Created: Dec, 04, 2024 11:04:05 by Wataru Fukuda

import watf.program_options
from watfio.AbstractParser import AbstractParser
from watfio.ConfigData import ConfigData

class FEMParser(AbstractParser):
  def __int__(self,filename):
    super().__init__(filename)
  def parse(self):
    option = watf.program_options.program_options()
    option.read(self.filename_)
    config = ConfigData('FEM', self.filename_)
    ### [info] section ###
    if(option.has_option('info','nn')):
      config.set('nn',int(option['info']['nn']))
    else:
      print("nn is not found in [info]")
      exit(1)
    if(option.has_option('info','ne')):
      config.set('ne',int(option['info']['ne']))
    else:
      print("ne is not found in [info]")
      exit(1)
    if(option.has_option('info','endian')):
      if(option['info']['endian']=='little'):
        config.set('endian','<')
      else:
        config.set('endian','>')
    else:
      print("endian is not found in [info]")
      exit(1)
    ### [mesh] section ###
    if(option.has_option('mesh','nen')):
      config.set('nen',int(option['mesh']['nen']))
    else:
      print("nen is not found in [mesh]")
      exit(1)
    if(option.has_option('mesh','npd')):
      config.set('npd',int(option['mesh']['npd']))
    else:
      print("npd is not found in [mesh]")
      exit(1)
    if(option.has_option('mesh','nsd')):
      config.set('nsd',int(option['mesh']['nsd']))
    else:
      print("nsd is not found in [mesh]")
      exit(1)
    ### [file] section ###
    if(option.has_option('file','xyz')):
      config.setFilepath('xyz',option['file']['xyz'])
      config.set('xyz',option['file']['xyz'])
    else:
      print("xyz is not found in [file]")
      exit(1)
    if(option.has_option('file','ien')):
      config.setFilepath('ien',option['file']['ien'])
      config.set('ien',option['file']['ien'])
    else:
      print("ien is not found in [file]")
      exit(1)
    if(option.has_option('file','rng')):
      config.setFilepath('rng',option['file']['rng'])
      config.set('rng',option['file']['rng'])
    return config

