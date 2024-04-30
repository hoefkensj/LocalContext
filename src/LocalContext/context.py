#!/usr/bin/env python
from LocalContext.typedef import LocalContext
from Clict import Clict
def New():
	global CTX
	def new(name='ctx'):
		nonlocal CTX
		CTX[name.lower()]=LocalContext()
		return CTX[name.lower()]
	return new

def Ctx(fn):
	def currentctx(*a,**k):
		return fn(ctx,*a,**k)
	return currentctx

if __name__ == '__main__':
	a=globals()
	print(a)