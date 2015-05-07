import numpy as np
import ipcv
import cv2

def rotate(blank, answer):
   numRows, numCols, numBands, dtype = ipcv.dimensions(blank)
   print 'blank:rows,cols', numRows, numCols
   numRowsA, numColsA, numBandsA, dataTypeA = ipcv.dimensions(answer)
   print 'answer:rows,cols', numRowsA, numColsA
   blankPTS = ipcv.circle(blank)
   answerPTS = ipcv.circle(answer)

   blankPTS.shape = (3, 3)
   answerPTS.shape = (3, 3)

   blankPTS = blankPTS[:, 0:2].astype(np.float32)
   answerPTS = answerPTS[:, 0:2].astype(np.float32)

   M = cv2.getAffineTransform(blankPTS, answerPTS)
   image = cv2.warpAffine(answer,M,(numCols,numRows))
   cv2.namedWindow('rotated',cv2.WINDOW_AUTOSIZE)
   cv2.imshow('rotated',image.astype(np.uint8))
   numRowsi, numColsi, numBandsi, dataTypei = ipcv.dimensions(image)
   print 'image:rows,cols:', numRowsi, numColsi
   cv2.waitKey()

   return image

if __name__ == '__main__':
   import cv2
   import numpy as np
   im1 = 'original.tif'
   im2 = 'gray0005.tif'
   blank = cv2.imread(im1)
   answer = cv2.imread(im2)
   rotated = ipcv.rotate(blank,answer)
   cv2.imwrite('registered0005.tif', rotated)
