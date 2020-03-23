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

def rgb2HEX(array):
    r = array[0]
    g = array[1]
    b = array[2]

    def toHex(num):
        hex_val = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        num_2 = int(num%16)
        num_1 = int((num - num_2)/16)
        num_hex = hex_val[num_1] + hex_val[num_2]
        return num_hex

    if(r<0 or g<0 or b<0 or r>255 or g>255 or b>255):
        print("Error, invalid input values")
        return [-1,-1,-1]

    hex_string = toHex(r) + toHex(g) + toHex(b)
    return(hex_string)

def HEX2rgb(hex_string):
    r_1 = hex_string[0]
    r_2 = hex_string[1]
    r = int(r_1,16) * 16 + int(r_2,16)

    g_1 = hex_string[2]
    g_2 = hex_string[3]
    g = int(g_1,16) * 16 + int(g_2,16)

    b_1 = hex_string[4]
    b_2 = hex_string[5]
    b = int(b_1,16) * 16 + int(b_2,16)

    return [r,g,b]

def rgb2cmyk(array):
    r = array[0]
    g = array[1]
    b = array[2]

    C = 0
    M = 0
    Y = 0
    K = 0

    if(r<0 or g<0 or b<0 or r>255 or g>255 or b>255):
        print("Error, invalid input values")
        return [-1,-1,-1]

    # Black
    if(r==0 & g==0 & b==0):
        K = 1
        return [C,M,Y,K]

    C = 1 - r/255
    M = 1 - g/255
    Y = 1 - b/255

    minCMY = min(C,min(M,Y))

    C = (C - minCMY) / (1 - minCMY)
    M = (M - minCMY) / (1 - minCMY)
    Y = (Y - minCMY) / (1 - minCMY)
    K = minCMY

    return [C,M,Y,K]

def HEX2cmyk(hex_string):
    return rgb2cmyk(HEX2rgb(hex_string))

def HEX2hsv(hex_string):
    return rgb2hsv(HEX2rgb(hex_string))

# print(rgb2cmyk([50,100,150]))
# print(rgb2cmyk([90,100,150]))
# HEX2rgb('5A6496')
# print(HEX2cmyk('5A6496'))


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
