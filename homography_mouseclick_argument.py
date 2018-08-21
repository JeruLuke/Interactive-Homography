# -*- coding: utf-8 -*-

import argparse
import cv2
import numpy as np
import os

path = os.getcwd()

list_pts = []
ix, iy = -1, -1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y#--- left button double click

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 7, (0, 255, 0), -1)
        list_pts.append([x, y])
        print(list_pts)
        if len(list_pts) == 4:
            print('There are 4 points : {}'.format(list_pts))
            cv2.imshow('Marked image.jpg', img)
            cv2.imwrite(os.path.join(path, 'results/Marked image.jpg'), img)
            
            pts_dst = np.array(list_pts, dtype = np.int32)
            print(pts_dst)
            h, status = cv2.findHomography(pts_src, pts_dst)      

            im_out = cv2.warpPerspective(im, h, (img.shape[1], img.shape[0]))
            cv2.imshow('Result.jpg', im_out)
            cv2.imwrite(os.path.join(path, 'results/warped.jpg'), im_out)
            
            r = cv2.drawContours(np.zeros_like(im_out), [pts_dst], 0, (255,255,255), -2)
            r = cv2.threshold(r[:,:,1], 0, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1]
            cv2.imshow("r", r)
            cv2.imwrite(os.path.join(path, 'results/mask.jpg'), r)
            
            masked = cv2.bitwise_and(img2, img2, mask = r)
            
            cv2.imshow("final", masked + im_out)
            cv2.imwrite(os.path.join(path, 'results/Spartacus_billboard.jpg'), masked + im_out)
            
            print('Homography Matrix: {}'.format(h))


ap = argparse.ArgumentParser()
ap.add_argument("-b", "--base_image", required=True,
	help="path to base image")
ap.add_argument("-s", "--inner_image", required=True,
	help="path to inner image")
args = vars(ap.parse_args())

im = cv2.imread(args["inner_image"], 1)

h, w, _ = im.shape
pts_src = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]])
    
img = cv2.imread(args["base_image"], 1)
img2 = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    cv2.imshow('small image', im)
    if cv2.waitKey(20) & 0xFF == 27:   #--- press 'ESC' to break
        break
    
cv2.destroyAllWindows()

