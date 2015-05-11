import numpy
import ipcv
import cv2
import cv
def paddingFiducials(answerSheet1, blankSheet1):
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
   
   numRowsF1, numColsF1, numBandsF1, dataTypeF1 = ipcv.dimensions(blankSheet)
   print numRowsF1, numColsF1

   pad = numpy.absolute(numRowsA - numColsA)/2.0
   maxCount = 255

   if (numRowsA-numColsA) % 2 != 0:
      answerSheet = numpy.pad(answerSheet, ((0,0),(pad,pad+1)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA-numColsA) % 2 == 0:
      answerSheet = numpy.pad(answerSheet, ((0,0),(pad,pad)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))

   numRowsAN, numColsAN, numBandsAN, dataTypeAN = ipcv.dimensions(answerSheet)

   pad_height1 = numpy.absolute(numRowsAN - numRowsF1)/2.0
   pad_width1 = numpy.absolute(numColsAN - numColsF1)/2.0
   maxCount = 255

   if (numRowsAN - numRowsF1) % 2 == 0 and (numColsAN - numColsF1) % 2 == 0:
      blankSheet = numpy.pad(blankSheet,((pad_height1, pad_height1),(pad_width1, pad_width1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsAN - numRowsF1) % 2 == 0 and (numColsAN - numColsF1) % 2 != 0:
      blankSheet = numpy.pad(blankSheet,((pad_height1, pad_height1),(pad_width1, pad_width1 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsAN - numRowsF1) %2 != 0 and (numColsAN - numColsF1) % 2 == 0:
      blankSheet = numpy.pad(blankSheet,((pad_height1, pad_height1 + 1),(pad_width1, pad_width1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   else:
      blankSheet = numpy.pad(blankSheet,((pad_height1, pad_height1 + 1),(pad_width1, pad_width1 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   print 'answerSheet shape:', answerSheet.shape

   return answerSheet, blankSheet

if __name__ == '__main__':
   #answerSheet1 = cv2.imread('gray0001.tif')
   answerSheet1 = cv2.imread('subtractedIm.tif')
   #############FOR HIGH RES##############
   #blankSheet1 = cv2.imread('original300dpi.tif')
   #############FOR LOW RES##############
   blankSheet1 = numpy.zeros((12,12))
   answerSheet, blankSheet = paddingFiducials(answerSheet1[385:704,72:133], blankSheet1)
   cv2.namedWindow('Fiducial1 Padded', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('Fiducial1 Padded', blankSheet.astype(numpy.uint8))
   cv2.waitKey()
   cv2.imwrite('boxPadded.tif', blankSheet)
   cv2.imwrite('answerSheet1.tif', answerSheet)

   action = ipcv.flush()
