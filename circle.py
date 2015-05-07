import numpy as np
import cv2
import ipcv
import cv
def circle(blank,answer):
   
   numRows,numCols,numBands, dtype = ipcv.dimensions(blank)
   img = cv2.medianBlur(blank,1)
   cimg = cv2.cvtColor(img,cv.CV_BGR2GRAY)
   img = cv2.cvtColor(img,cv.CV_BGR2GRAY)
   mask = np.zeros((numRows,numCols)).astype(np.uint8)
   mask[690:773,19:105] = 1
   mask[15:100,512:603] = 1
   mask[700:780,490:590] = 1
   img = img*mask

   circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,40,
                                     param1=50,param2=20,minRadius=7,maxRadius=24)
   print circles
   circles = np.uint16(np.around(circles))
   for i in circles[0,:]:
    #  draw the outer circle
      cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
     # draw the center of the circle
      cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

 #     cv2.imwrite('cimg.tif',cimg)
      cv2.imwrite('cimg.tif',cimg)
      cv2.namedWindow('detected circles',cv2.CV_WINDOW_AUTOSIZE)
      cv2.imshow('detected circles',cimg)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
      
      
if __name__ == '__main__':
   import numpy
   import cv2

#   im1 = 'original.tif'
   im1 = 'black0008.tif'
   im2 = 'test0000.tif'
   blank = cv2.imread(im1)
   answer = cv2.imread(im2)
   new = ipcv.circle(blank,answer)





