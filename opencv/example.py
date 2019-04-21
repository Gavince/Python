# -*- coding: utf-8 -*-
# 行人检测
import cv2
import numpy as np


def svmdetectperson(img):
    hog=cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    person,w= hog.detectMultiScale(img)
    return person


def is_inside(a,b):
    x1,y1,w1,h1=a
    x2,y2,w2,h2=b #judge b  is not include a
    return x1>x2 and y1>y2 and x1+w1<x2+w2 and y1+h1<y2+h2


def draw(img,a):
    x,y,w,h=a
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)


if __name__=="__main__":
    img=cv2.imread("/home/gavin/Downloads/5.jpg")
    person=svmdetectperson(img)
    filtered=[]
    for i,p in enumerate(person):
        for j,p1 in enumerate(person):
            if i!=j and is_inside(p,p1):
                break
        filtered.append(p)
    for p in filtered:
        draw(img,p)
    cv2.imshow("person",img)
    cv2.waitKey(0)
