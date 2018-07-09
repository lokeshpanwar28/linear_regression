#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 18:04:02 2018

@author: lokesh
"""
from matplotlib import pyplot
import numpy as np
data = np.genfromtxt('train.csv',delimiter=",")
#print csv[1:,0]
xx=data[1:,0]
yy=data[1:,1]
N = len(xx)
x = xx/np.amax(xx)
y = yy/np.amax(yy)
pyplot.figure(1)
pyplot.plot(x,y,'.')
#all_m=np.zeros([30,2])
max_iter=5000
all_fun=np.zeros(max_iter)
#for j in range(1,30):
m = np.random.rand(2)
for i in range(0,max_iter):
    # defining the slop of the cost function
    m -= (0.03/N)*np.array([sum((m[0]*x+m[1]*np.ones(N)-y)*x),sum((m[0]*x+m[1]*np.ones(N)-y))],dtype=float)
    # function calculation end of the all iteration
    fun = (sum((m[0]*x+m[1]*np.ones(N)-y)**2))
    all_fun[i]=fun
#    all_m[j,:]=m
# show the 30 vale generated with this gradient based method
#print all_fun[1:],all_m[1:,:]
#print np.amin(all_fun[1:]),all_m[1:,:]
print "training error=", fun/(2*N)
pyplot.figure(2)
pyplot.plot(all_fun,'-')

test_data = np.genfromtxt('test.csv',delimiter=",")
test_xx=test_data[1:,0]
test_yy=test_data[1:,1]
x = test_xx/np.amax(xx)
y = test_yy/np.amax(yy)
N = len(x)
y_predicted=m[0]*x+m[1]*np.ones(N)
pred_error=sum((y-y_predicted)**2)
print "prediction error=", pred_error/(2*N)
pyplot.figure(3)
pyplot.plot((y-y_predicted))