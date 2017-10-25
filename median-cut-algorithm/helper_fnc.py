import cv2
import numpy as np

path = "code_blooded.bmp"

def binarySearch(encode,l,h,x):
    " ceil binary search returns index and -1 if not present "
    if l>h:
        return -1
    if x>=(encode[h]):
        return h
    mid = int((l+h)/2)
    if encode[mid]==x:
        return mid
    if mid>0 and (encode[mid-1])<=x and x<(encode[mid]):
        return mid-1
    if x<(encode[mid]):
        return binarySearch(encode,l,mid-1,x)
    return binarySearch(encode,mid+1,h,x)

def flatten_image(image):
    " flatten an image from 2d to 1d array "
    flat = []
    flat = [x for sublist in image for x in sublist]
    flat = np.array(flat)
    return flat

def median_cut(img,depth):
    "This function decreases the number of bits required to 2^depth"
    img = flatten_image(img)
    img.sort()
    n = len(img)
    encode = []
    x = int(n/pow(2,depth))
    for i in range(0,pow(2,depth)):
        encode.append(img[i*x])
    encode.append(img[n-1])
    return encode

def SNR(original_img,compressed_img,rows,cols):
    "diff between original img and compressed img"
    noise = [[0 for x in range(rows)] for y in range(cols)]
    for i in range(rows):
        for j in range(cols):
            if(original_img[i][j]>compressed_img[i][j]):
                noise[i][j]=original_img[i][j]-compressed_img[i][j]
            else:
                noise[i][j]=(compressed_img[i][j]-original_img[i][j])
                noise[i][j]*=-1
    return noise
