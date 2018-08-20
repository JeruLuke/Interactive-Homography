#--- To draw circle upon double clicking left mouse button ---

import cv2
import numpy as np
import os

path = r'C:\Users\selwyn77\Desktop\Stack\Homography'

list_pts = []
ix, iy = -1, -1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y#--- left button double click

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
        list_pts.append([x, y])
        print(list_pts)
        if len(list_pts) == 4:
            print('There are 4 points : {}'.format(list_pts))
            pts_dst = np.array(list_pts, dtype = np.int32)
            print(pts_dst)
            h, status = cv2.findHomography(pts_src, pts_dst)
            
#            for j in pts_dst:
#            cv2.drawContours(drawing, contours , 0, (255, 255, 255), -1)                
#            r = cv2.drawContours(np.zeros(img.shape, np.uint8), [pts_dst], 0, (255, 255, 255), -1)
#            cv2.imshow('r.jpg', r)
#            th = cv2.threshold(r[:,:,1], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#            cv2.imshow('th.jpg', th)
            
#            for cnt in contours:
#    if (cv2.contourArea(cnt) > 100):
#                x, y, w, h = cv2.boundingRect(cnt)            
            
#            r_gray, contours, hierarchy = cv2.findContours(cv2.threshold(r[:,:,1], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#            cv2.imshow('r_gray.jpg', r_gray)        
#            print r
#            cv2.drawContours(img.copy(), contours , 0, (255, 255, 255), -1)            
            

            im_out = cv2.warpPerspective(im, h, (img.shape[1], img.shape[0]))
            cv2.imshow('Result.jpg', im_out)
            
            r = cv2.drawContours(np.zeros_like(im_out), [pts_dst], 0, (255,255,255), -2)
            r = cv2.threshold(r[:,:,1], 0, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1]
            cv2.imshow("r", r)
            
            masked = cv2.bitwise_and(img2, img2, mask = r)
            
            cv2.imshow("final", masked + im_out)
            
            print('Homography Matrix: {}'.format(h))
#        print('Coordinates:', x, y)
#        list_pts.append((x, y))
#        print('Length : {}'.format(len(list_pts)))
        
#        if len(list_pts) <= 4:
#            list_pts.append([x, y])
#        elif len(list_pts) > 4:
#            print('You selected an additional coordinate. Please choose 4 coordinate points ONLY')
#            list_pts[:] = []
        
#        print('List : {}'.format(list_pts))
        
# Create a black image, a window and bind the function to window


im = cv2.imread(os.path.join(path, 'board.jpg'), 1)
h, w, _ = im.shape
pts_src = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]])
    
#w, h, _ = im.shape
#pts_src = np.array([[0, 0], [h-1, 0], [h-1, w-1], [0, w-1]])

img = cv2.imread(os.path.join(path, 'street.jpg'), 1)
img2 = img.copy()
#img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(0) & 0xFF == 27:   #--- press 'ESC' to break
        break
    
cv2.destroyAllWindows()

