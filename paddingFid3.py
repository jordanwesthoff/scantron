import numpy
import ipcv
import cv2
import cv
def paddingFid3(answerSheet1, blankSheet1):
   numRowsA, numColsA, numBandsA, dataTypeA = ipcv.dimensions(answerSheet1)
   numRowsB, numColsB, numBandsB, dataTypeB = ipcv.dimensions(blankSheet1)
   if numBandsA == 3:
      answerSheet = cv2.cvtColor(answerSheet1, cv.CV_BGR2GRAY)
   elif numBandsA == 1:
      answerSheet = answerSheet1

   if numBandsB == 3:
      blankSheet = cv2.cvtColor(blankSheet1, cv.CV_BGR2GRAY)
   elif numBandsB == 1:
      blankSheet = blankSheet1
   
   ################FOR LOW RES##################### 
   #Top Right Fiducial
   #fiducial3a = blankSheet[29:78,621:670]
   fiducial3a = blankSheet[29:78,531:579]
   
   numRowsF3, numColsF3, numBandsF3, dataTypeF3 = ipcv.dimensions(fiducial3a)
   
   numRowsAN, numColsAN, numBandsAN, dataTypeAN = ipcv.dimensions(answerSheet)

   pad_height3 = numpy.absolute(numRowsAN - numRowsF3)/2.0
   pad_width3 = numpy.absolute(numColsAN - numColsF3)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsAN - numRowsF3) % 2 == 0 and (numColsAN - numColsF3) % 2 == 0:
      fiducial3 = numpy.pad(fiducial3a,((pad_height3, pad_height3),(pad_width3, pad_width3)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsAN - numRowsF3) % 2 == 0 and (numColsAN - numColsF3) % 2 != 0:
      fiducial3 = numpy.pad(fiducial3a,((pad_height3, pad_height3),(pad_width3, pad_width3 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsAN - numRowsF3) %2 != 0 and (numColsAN - numColsF3) % 2 == 0:
      fiducial3 = numpy.pad(fiducial3a,((pad_height3, pad_height3 + 1),(pad_width3, pad_width3)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   else:
      fiducial3 = numpy.pad(fiducial3a,((pad_height3, pad_height3 + 1),(pad_width3, pad_width3 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
  

   cv2.imwrite('fiducial3.tif', fiducial3)

   return fiducial3

if __name__ == '__main__':
   #answerSheet1 = cv2.imread('gray0001.tif')
   answerSheet1 = cv2.imread('black0007.tif')
   #############FOR HIGH RES##############
   #blankSheet1 = cv2.imread('original300dpi.tif')
   #############FOR LOW RES##############
   blankSheet1 = cv2.imread('original.tif')
   fiducial3 = paddingFid3(answerSheet1, blankSheet1)
   '''
   cv2.namedWindow('Fiducial1 Padded', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('Fiducial1 Padded', fiducial1.astype(numpy.uint8))
   cv2.waitKey()
   cv2.namedWindow('Answer Sheet', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('Answer Sheet', fiducial3)
   cv2.imwrite('fiducial1.tif', fiducial1)
   cv2.imwrite('fiducial2.tif', fiducial2)
   cv2.imwrite('fiducial3.tif', fiducial3)
   cv2.imwrite('answerSheet1.tif', answerSheet)
   '''
   action = ipcv.flush()
