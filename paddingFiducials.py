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
   
   #Bottom Left Fiducial
   fiducial1a = blankSheet[717:759,38:81]
   #Bottom Right Fiducial
   fiducial2a = blankSheet[714:762,517:567]
   #Top Right Fiducial
   fiducial3a = blankSheet[27:78,519:581]
   numRowsF1, numColsF1, numBandsF1, dataTypeF1 = ipcv.dimensions(fiducial1a)
   numRowsF2, numColsF2, numBandsF2, dataTypeF2 = ipcv.dimensions(fiducial2a)
   numRowsF3, numColsF3, numBandsF3, dataTypeF3 = ipcv.dimensions(fiducial3a)
   print numRowsF1, numColsF1

   pad_height1 = numpy.absolute(numRowsA - numRowsF1)/2.0
   pad_width1 = numpy.absolute(numColsA - numColsF1)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsA - numRowsF1) % 2 == 0 and (numColsA - numColsF1) % 2 == 0:
      fiducial1 = numpy.pad(fiducial1a,((pad_height1, pad_height1),(pad_width1, pad_width1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA - numRowsF1) % 2 == 0 and (numColsA - numColsF1) % 2 != 0:
      fiducial1 = numpy.pad(fiducial1a,((pad_height1, pad_height1),(pad_width1, pad_width1 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA - numRowsF1) %2 != 0 and (numColsA - numColsF1) % 2 == 0:
      fiducial1 = numpy.pad(fiducial1a,((pad_height1, pad_height1 + 1),(pad_width1, pad_width1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   else:
      fiducial1 = numpy.pad(fiducial1a,((pad_height1, pad_height1 + 1),(pad_width1, pad_width1 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   print 'fiducial1 shape:', fiducial1.shape
   print 'answerSheet shape:', answerSheet.shape

   pad_height2 = numpy.absolute(numRowsA - numRowsF2)/2.0
   pad_width2 = numpy.absolute(numColsA - numColsF2)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsA - numRowsF2) % 2 == 0 and (numColsA - numColsF2) % 2 == 0:
      fiducial2 = numpy.pad(fiducial2a,((pad_height2, pad_height2),(pad_width2, pad_width2)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA - numRowsF2) % 2 == 0 and (numColsA - numColsF2) % 2 != 0:
      fiducial2 = numpy.pad(fiducial2a,((pad_height2, pad_height2),(pad_width2, pad_width2 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA - numRowsF2) %2 != 0 and (numColsA - numColsF2) % 2 == 0:
      fiducial2 = numpy.pad(fiducial2a,((pad_height2, pad_height2 + 1),(pad_width2, pad_width2)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   else:
      fiducial2 = numpy.pad(fiducial2a,((pad_height2, pad_height2 + 1),(pad_width2, pad_width2 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   print 'fiducial2 shape:', fiducial2.shape
   print 'answerSheet shape:', answerSheet.shape

   pad_height3 = numpy.absolute(numRowsA - numRowsF3)/2.0
   pad_width3 = numpy.absolute(numColsA - numColsF3)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsA - numRowsF3) % 2 == 0 and (numColsA - numColsF3) % 2 == 0:
      fiducial3 = numpy.pad(fiducial3a,((pad_height3, pad_height3),(pad_width3, pad_width3)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA - numRowsF3) % 2 == 0 and (numColsA - numColsF3) % 2 != 0:
      fiducial3 = numpy.pad(fiducial3a,((pad_height3, pad_height3),(pad_width3, pad_width3 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA - numRowsF3) %2 != 0 and (numColsA - numColsF3) % 2 == 0:
      fiducial3 = numpy.pad(fiducial3a,((pad_height3, pad_height3 + 1),(pad_width3, pad_width3)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   else:
      fiducial3 = numpy.pad(fiducial3a,((pad_height3, pad_height3 + 1),(pad_width3, pad_width3 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   print 'fiducial3 shape:', fiducial3.shape
   print 'answerSheet shape:', answerSheet.shape

   return fiducial1

if __name__ == '__main__':
   answerSheet1 = cv2.imread('gray0001.tif')
   blankSheet1 = cv2.imread('original.tif')
   fiducial1 = paddingFiducials(answerSheet1, blankSheet1)
   cv2.namedWindow('Fiducial1 Padded', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('Fiducial1 Padded', fiducial1.astype(numpy.uint8))
   cv2.waitKey()
   cv2.namedWindow('Answer Sheet', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('Answer Sheet', answerSheet1)
   action = ipcv.flush()
