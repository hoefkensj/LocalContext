#!/usr/bin/env python

from typedef import LocalContext
from Clict import Clict
if not globals().get('CTX'):
	globals()['CTX']=Clict()
