#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:05:12 2019

@author: gavin
"""

import fire
class Test(object):
	"""A simple test"""
	def hello(self, name = "word"):

		return ("Hello %s" % name)


if __name__ == "__main__":
    fire.Fire(Test)
