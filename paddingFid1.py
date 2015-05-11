import numpy
import ipcv
import cv2
import cv
def paddingFid1(answerSheet1, blankSheet1):
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
   #Bottom Left Fiducial
   #fiducial1a = blankSheet[717:759,129:171]
   fiducial1a = blankSheet[717:759,38:81]
   
   numRowsF1, numColsF1, numBandsF1, dataTypeF1 = ipcv.dimensions(fiducial1a)

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

   return fiducial1

if __name__ == '__main__':
   #answerSheet1 = cv2.imread('gray0001.tif')
   answerSheet1 = cv2.imread('black0007.tif')
   #############FOR HIGH RES##############
   #blankSheet1 = cv2.imread('original300dpi.tif')
   #############FOR LOW RES##############
   blankSheet1 = cv2.imread('original.tif')
   fiducial1 = paddingFid1(answerSheet1, blankSheet1)
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
