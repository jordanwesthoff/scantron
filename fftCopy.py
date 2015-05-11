import cv2
import numpy
import ipcv
import cv
def fftCorrelation(fiducial1C, blankSheetC):
   
   numRows, numCols, numBands, dataType = ipcv.dimensions(blankSheetC)
   numRows1, numCols1, numBands1, dataType1 = ipcv.dimensions(fiducial1C)
   print 'blank bands:', numBands
   print 'fiducial1 bands:', numBands1

   if numBands == 3:
      blankSheet = cv2.cvtColor(blankSheetC, cv.CV_BGR2GRAY)
   elif numBands == 1:
      blankSheet = blankSheetC

   if numBands1 == 3:
      fiducial1 = cv2.cvtColor(fiducial1C, cv.CV_BGR2GRAY)
   elif numBands2 == 1:
      fiducial1 = fiducial1C

   freqFid1 = numpy.fft.fft2(fiducial1)
   freqBlank = numpy.fft.fft2(blankSheet)

   magFid1 = numpy.absolute(freqFid1)
   magBlank = numpy.absolute(freqBlank)

   phaseFid1 = numpy.angle(freqFid1)
   phaseBlank = numpy.angle(freqBlank)

   correlation = magBlank * magFid1 * numpy.exp(1j * (phaseBlank - phaseFid1))
 
   corrSpat = numpy.fft.ifft2(correlation)
   corrSpat = numpy.absolute(numpy.fft.fftshift(corrSpat))

   print corrSpat
   dispCorrSpat = corrSpat / numpy.max(corrSpat)

   print dispCorrSpat.max(), dispCorrSpat.min()
   
   numberRows, numberColumns, numberBands, dataType1 = ipcv.dimensions(blankSheet)
   numIncorrect = numpy.zeros((numberRows, numberColumns))
   threshold = 0.9999999999999997226
   #
   numIncorrect[dispCorrSpat < threshold] = 0
   #if response is greater than/equal to the threshold, a match occurs
   numIncorrect[dispCorrSpat >= threshold] = 1
   print numIncorrect
   totalIncorrect = numpy.sum(numIncorrect)
   print 'totalIncorrect', totalIncorrect    
   
   cv2.namedWindow('corrSpat', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('corrSpat', dispCorrSpat)
   cv2.waitKey() 

   locationMax = numpy.argmax(corrSpat)
   rowLoc, colLoc = numpy.unravel_index(locationMax, (numRows, numCols))
   displayIm = cv2.merge((blankSheet, blankSheet, blankSheet))
   print rowLoc, colLoc

   displayIm[rowLoc - 1:rowLoc+2, colLoc-1:colLoc+2, 2] = 0
   displayIm[rowLoc-1:rowLoc+2, colLoc-1:colLoc+2, 0:1] = 255

   cv2.namedWindow('displayIm', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('displayIm', displayIm)
   cv2.waitKey()
   cv2.imwrite('dotsInCir3.tif', displayIm)
   '''
   fftFid1 = numpy.fft.ifftshift(centerFreqFid1)
   fftBlank = numpy.fft.ifftshift(centerFreqBlank)
   Fid1 = numpy.fft.ifft2(fftFid1)
   Blank = numpy.fft.ifft2(fftBlank)
   '''
   return rowLoc, colLoc

if __name__ == '__main__':
   fiducial1C = cv2.imread('boxPadded.tif')
   blankSheetC = cv2.imread('answerSheet1.tif')
   fftCorrelation(fiducial1C, blankSheetC)