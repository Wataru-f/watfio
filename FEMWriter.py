#!/usr/bin/env python3
# Created: Dec, 07, 2024 21:36:47 by Wataru Fukuda

from watfio.AbstractWriter import AbstractWriter

class FEMWriter(AbstractWriter):
  DATA_TYPE={
   "xyz" :("mxyz", "f", "n", True),
   "ien" :("mien", "i", "e", True),
   "rng" :("mrng", "i", "e", False)
  }
  REMAKE_MAP={
    "nn"    : ("info","nn"),
    "ne"    : ("info","ne"),
    "endian": ("info","endian"),
    "nen"   : ("mesh","nen"),
    "npd"   : ("mesh","npd"),
    "nsd"   : ("mesh","nsd")
  }

