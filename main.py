import numpy as np



def rgb2hsv(array):

    r = array[0]
    g = array[1]
    b = array[2]

    H = 0
    S = 0
    V = 0

    if(r<0 or g<0 or b<0 or r>255 or g>255 or b>255):
        print("Error, invalid input values")
        return [-1,-1,-1]

    r = r/255
    g = g/255
    b = b/255

    minVal = min(r,min(g,b))
    maxVal = max(r,max(g,b))

    # Black and white colors
    if(minVal == maxVal):
        H = 0
        S = 0
        V = minVal
        return [H,S,V]

    # Other Color Values
    if(r == minVal):
        d = g - b
        h = 3
    elif(b == minVal):
        d = r - g
        h = 1
    else:
        d = b - r
        h = 5

    H = 60 * (h - d / (maxVal - minVal))
    S = (maxVal - minVal)/maxVal
    V = maxVal


    return [H,S,V]



print(rgb2hsv([50,100,150]))

# List of color spaces to implement
# HEX
# RGB
# BGR
# LAB
# CMYK
# RGBA
# HSL
# CIE
# sRGB
# ICtCp
# TSL
# NCS
# PMS
# xvYCC
# YPbPr
# YIQ
