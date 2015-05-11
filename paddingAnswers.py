import numpy
import ipcv
import cv2
import cv
def paddingAnswers(answerSheet1, blankSheet1):
   numRowsA, numColsA, numBandsA, dataTypeA = ipcv.dimensions(answerSheet1)
   numRowsB, numColsB, numBandsB, dataTypeB = ipcv.dimensions(blankSheet1)
   print numRowsB, numColsB
   if numBandsA == 3:
      answerSheet = cv2.cvtColor(answerSheet1, cv.CV_BGR2GRAY)
   elif numBandsA == 1:
      answerSheet = answerSheet1

   if numBandsB == 3:
      blankSheet = cv2.cvtColor(blankSheet1, cv.CV_BGR2GRAY)
   elif numBandsB == 1:
      blankSheet = blankSheet1  

   pad = numpy.absolute(numRowsA - numColsA)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsA-numColsA) % 2 != 0:
      answerSheet = numpy.pad(answerSheet, ((0,0),(pad,pad+1)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA-numColsA) % 2 == 0:
      answerSheet = numpy.pad(answerSheet, ((0,0),(pad,pad)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))

   pad1 = numpy.absolute(numRowsB - numColsB)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsB-numColsB) % 2 != 0:
      blankSheet = numpy.pad(blankSheet, ((0,0),(pad1,pad1+1)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA-numColsA) % 2 == 0:
      blankSheet = numpy.pad(blankSheet, ((0,0),(pad1,pad1)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))


   return answerSheet, blankSheet

if __name__ == '__main__':
   #answerSheet1 = cv2.imread('gray0001.tif')
   answerSheet1 = cv2.imread('black0007.tif')
   #############FOR HIGH RES##############
   #blankSheet1 = cv2.imread('original300dpi.tif')
   #############FOR LOW RES##############
   blankSheet1 = cv2.imread('original.tif')
   answerSheet, blankSheet = paddingAnswers(answerSheet1, blankSheet1)
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
