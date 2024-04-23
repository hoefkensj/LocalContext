#!/usr/bin/env python
from LocalContext.typedef import LocalContext
from Clict import Clict
def New():
	localctx=Clict()
	def new(name='ctx'):
		nonlocal localctx
		ctx=LocalContext()
		localctx[f'ctx_{name}']=ctx
		return ctx
	return new
def CurrentCtx(fn):
	def currentctx(*a,**k)
		return fn(ctx,*a,**k)
	return currentctx
	def main():
	pass


if __name__ == '__main__':
	a=globals()
	print(a)