import cv2
import numpy as np
from helper_fnc import *

path = "code_blooded.bmp"
img = cv2.imread(path)

#resized_image = cv2.resize(img, (256, 256))
#cv2.imwrite('code_blooded.bmp',resized_image)

img = np.array(img)
cv2.imshow('image_original',img)
rows,cols,channel = img.shape
img_b,img_g,img_r = cv2.split(img)
o_img_b,o_img_g,o_img_r = cv2.split(img)

depth = 5

nodes = pow(2,depth)
g_encode = median_cut(img_g,depth)
b_encode = median_cut(img_b,depth)
r_encode = median_cut(img_r,depth)

#np.savetxt("green.csv", img_g, delimiter=",")
#np.savetxt("blue.csv", img_b, delimiter=",")
#np.savetxt("red.csv", img_r, delimiter=",")

#lookup table creation
with open('lookup32.csv','w') as file:
    file.write("Green lookup:\n")
    file.write("Start,End,Value\n")
    for i in range(nodes):
        file.write(str(g_encode[i])+','+str(g_encode[i+1])+','+str(int(g_encode[i]/2+g_encode[i+1]/2)))
        file.write('\n')
    file.write("Blue lookup:\n")
    file.write("Start,End,Value\n")
    for i in range(nodes):
        file.write(str(b_encode[i])+','+str(b_encode[i+1])+','+str(int(b_encode[i]/2+b_encode[i+1]/2)))
        file.write('\n')
    file.write("Red lookup:\n")
    file.write("Start,End,Value\n")
    for i in range(nodes):
        file.write(str(r_encode[i])+','+str(r_encode[i+1])+','+str(int(r_encode[i]/2+r_encode[i+1]/2)))
        file.write('\n')

for i in range(rows):
    for j in range(cols):
        index = binarySearch(b_encode,0,nodes-1,img_b[i][j])
        if(index!=-1):
            img_b[i][j] = int(b_encode[index]/2+b_encode[index+1]/2)
        index = binarySearch(g_encode,0,nodes-1,img_g[i][j])
        if(index!=-1):
            img_g[i][j] = int(g_encode[index]/2+g_encode[index+1]/2)
        index = binarySearch(r_encode,0,nodes-1,img_r[i][j])
        if(index!=-1):
            img_r[i][j] = int(r_encode[index]/2+r_encode[index+1]/2)

rgb = np.dstack((img_b,img_g,img_r))
cv2.imshow('image_compressed',rgb)

#np.savetxt("noise_green16.csv", SNR(o_img_g,img_g,rows,cols), delimiter=",")
#np.savetxt("noise_blue16.csv", SNR(o_img_b,img_b,rows,cols), delimiter=",")
#np.savetxt("noise_red16.csv", SNR(o_img_r,img_r,rows,cols), delimiter=",")

#cv2.imwrite('code_blooded16.bmp',rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
