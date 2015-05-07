import numpy as np
import cv2
import ipcv
import cv
def circle(blank,answer):
   
#   numRows,numCols,numBands, dtype = ipcv.dimensions(blank)
#   numRowsn,numColsn,numBandsn, dtypen = ipcv.dimensions(answer)
#   if numBands == 3:
#      blank = cv2.cvtColor(blank,cv.CV_BGR2GRAY)
#   if numBandsn == 3:
#      answer = cv2.cvtColor(answer,cv.CV_BGR2GRAY)
   '''
   blank = blank.astype(numpy.uint8)
   print blank.shape
   print answer.shape
   im1 = cv2.HoughCircles(blank,cv.CV_HOUGH_GRADIENT,dp=1,minDist=2)#,minRadius=4,maxRadius=101) 
   print im1
   '''
  # img = cv2.imread('opencv_logo.png',0)
   img = cv2.medianBlur(blank,3)
   cimg = cv2.cvtColor(img,cv.CV_BGR2GRAY)
   img = cv2.cvtColor(img,cv.CV_BGR2GRAY)
   circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,40,
                                     param1=50,param2=25,minRadius=7,maxRadius=24)
   print circles
   circles = np.uint16(np.around(circles))
   for i in circles[0,:]:
    #  draw the outer circle
      cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
     # draw the center of the circle
      cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

 #     cv2.imwrite('cimg.tif',cimg)
      cv2.namedWindow('detected circles',cv2.CV_WINDOW_AUTOSIZE)
      cv2.imshow('detected circles',cimg)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
if __name__ == '__main__':
   import numpy
   import cv2

   im1 = 'original.tif'
   im2 = 'test0000.tif'
   blank = cv2.imread(im1)
   answer = cv2.imread(im2)
   new = ipcv.circle(blank,answer)





