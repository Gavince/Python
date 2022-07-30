# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:36:41 2017

@author: Gavin
"""

import numpy as np
A=np.array([[1,2,30],
            [4,6,5]],dtype = np.int64)
print(A.shape)
print(A.flatten())  #降维
print(A.ndim)
print(A.dtype)
B = np.zeros((5,6))
print(B)
C=np.empty((1,2))
print(C)
print(np.arange(12).reshape((3,4)))
print(B.size)#看元素个数
print(np.linspace(1,33,5))
print(np.max(A,axis=1))#1表示行方向
print(np.sum(A,axis=0))

arr=[  value  for value in range(1,6)]
print(arr)