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

   ################FOR HIGH RES####################
   #Bottom Left Fiducial
   #fiducial1a = blankSheet[2993:3162,167:337]
   #Bottom Right Fiducial
   #fiducial2a = blankSheet[2980:3174,2163:2356]
   #Top Right Fiducial
   #fiducial3a = blankSheet[120:323,2214:2416]
   
   ################FOR LOW RES##################### 
   #Bottom Left Fiducial
   fiducial1a = blankSheet[717:759,38:81]
   #Bottom Right Fiducial
   fiducial2a = blankSheet[714:762,517:567]
   #Top Right Fiducial
   fiducial3a = blankSheet[29:78,531:579]
   
   numRowsF1, numColsF1, numBandsF1, dataTypeF1 = ipcv.dimensions(fiducial1a)
   numRowsF2, numColsF2, numBandsF2, dataTypeF2 = ipcv.dimensions(fiducial2a)
   numRowsF3, numColsF3, numBandsF3, dataTypeF3 = ipcv.dimensions(fiducial3a)
   print numRowsF1, numColsF1

   pad = numpy.absolute(numRowsA - numColsA)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsA-numColsA) % 2 != 0:
      answerSheet = numpy.pad(answerSheet, ((0,0),(pad,pad+1)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA-numColsA) % 2 == 0:
      answerSheet = numpy.pad(answerSheet, ((0,0),(pad,pad)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))

   numRowsAN, numColsAN, numBandsAN, dataTypeAN = ipcv.dimensions(answerSheet)

   pad_height1 = numpy.absolute(numRowsAN - numRowsF1)/2.0
   pad_width1 = numpy.absolute(numColsAN - numColsF1)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsAN - numRowsF1) % 2 == 0 and (numColsAN - numColsF1) % 2 == 0:
      fiducial1 = numpy.pad(fiducial1a,((pad_height1, pad_height1),(pad_width1, pad_width1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsAN - numRowsF1) % 2 == 0 and (numColsAN - numColsF1) % 2 != 0:
      fiducial1 = numpy.pad(fiducial1a,((pad_height1, pad_height1),(pad_width1, pad_width1 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsAN - numRowsF1) %2 != 0 and (numColsAN - numColsF1) % 2 == 0:
      fiducial1 = numpy.pad(fiducial1a,((pad_height1, pad_height1 + 1),(pad_width1, pad_width1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   else:
      fiducial1 = numpy.pad(fiducial1a,((pad_height1, pad_height1 + 1),(pad_width1, pad_width1 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   print 'fiducial1 shape:', fiducial1.shape
   print 'answerSheet shape:', answerSheet.shape

   pad_height2 = numpy.absolute(numRowsAN - numRowsF2)/2.0
   pad_width2 = numpy.absolute(numColsAN - numColsF2)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsAN - numRowsF2) % 2 == 0 and (numColsAN - numColsF2) % 2 == 0:
      fiducial2 = numpy.pad(fiducial2a,((pad_height2, pad_height2),(pad_width2, pad_width2)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsAN - numRowsF2) % 2 == 0 and (numColsAN - numColsF2) % 2 != 0:
      fiducial2 = numpy.pad(fiducial2a,((pad_height2, pad_height2),(pad_width2, pad_width2 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsAN - numRowsF2) %2 != 0 and (numColsAN - numColsF2) % 2 == 0:
      fiducial2 = numpy.pad(fiducial2a,((pad_height2, pad_height2 + 1),(pad_width2, pad_width2)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   else:
      fiducial2 = numpy.pad(fiducial2a,((pad_height2, pad_height2 + 1),(pad_width2, pad_width2 + 1)), 'constant', constant_values = ((maxCount, maxCount),(maxCount,maxCount)))
   print 'fiducial2 shape:', fiducial2.shape
   print 'answerSheet shape:', answerSheet.shape

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
   print 'fiducial3 shape:', fiducial3.shape
   print 'answerSheet shape:', answerSheet.shape

   pad1 = numpy.absolute(numRowsB - numColsB)/2.0
   maxCount = numpy.max(blankSheet)

   if (numRowsB-numColsB) % 2 != 0:
      blankSheet = numpy.pad(blankSheet, ((0,0),(pad1,pad1+1)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))
   elif (numRowsA-numColsA) % 2 == 0:
      blankSheet = numpy.pad(blankSheet, ((0,0),(pad1,pad1)), 'constant', constant_values=((maxCount, maxCount),(maxCount,maxCount)))

   cv2.imwrite('paddedBlank.tif', blankSheet)

   return fiducial1, fiducial2, fiducial3, answerSheet

if __name__ == '__main__':
   #answerSheet1 = cv2.imread('gray0001.tif')
   answerSheet1 = cv2.imread('gray0001.tif')
   #############FOR HIGH RES##############
   #blankSheet1 = cv2.imread('original300dpi.tif')
   #############FOR LOW RES##############
   blankSheet1 = cv2.imread('original.tif')
   fiducial1, fiducial2, fiducial3, answerSheet = paddingFiducials(answerSheet1, blankSheet1)
   cv2.namedWindow('Fiducial1 Padded', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('Fiducial1 Padded', fiducial1.astype(numpy.uint8))
   cv2.waitKey()
   cv2.namedWindow('Answer Sheet', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('Answer Sheet', fiducial3)
   cv2.imwrite('fiducial1.tif', fiducial1)
   cv2.imwrite('fiducial2.tif', fiducial2)
   cv2.imwrite('fiducial3.tif', fiducial3)
   cv2.imwrite('answerSheet1.tif', answerSheet)

   action = ipcv.flush()
