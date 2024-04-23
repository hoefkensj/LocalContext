#!/usr/bin/env python

from Clict import  Clict

class LocalContext(Clict):
	def __getitem__(s, i):
		return s.__getitem__(i)
	def __getattr__(s, i):
		return super().__getattr__(i)
	def __setitem__(s, k,v):
		super().__setitem__(k,v)
	def __setattr__(s, k,v):
		s.__setitem__(k,v)
def main():
	pass


if __name__ == '__main__':
	main()
