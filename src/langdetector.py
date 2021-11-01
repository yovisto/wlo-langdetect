# -*- coding: utf-8 -*-
import os, sys, langdetect

class LangDetector:

	def __init__(self):
		langdetect.DetectorFactory.seed = 0

	def detect(self, text):
		r = {}
		try:
			for l in langdetect.detect_langs(text):
				r[l.lang]=l.prob
		except:
			pass
		return r



if __name__ == '__main__':	

	text = sys.argv[1]

	p = LangDetector()

	for l,p in p.detect(text).items():
		print (l,p)

	