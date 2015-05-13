import cv2
import numpy
import ipcv
import cv
def fftCorrelation(fiducial1C, fiducial2C, fiducial3C, blankSheetC):
   
   numRows, numCols, numBands, dataType = ipcv.dimensions(blankSheetC)
   numRows1, numCols1, numBands1, dataType1 = ipcv.dimensions(fiducial1C)
   numRows2, numCols2, numBands2, dataType2 = ipcv.dimensions(fiducial2C)
   numRows3, numCols3, numBands3, dataType3 = ipcv.dimensions(fiducial3C)
   print 'blank bands:', numBands
   print 'fiducial1 bands:', numBands1
   print 'fiducial2 bands:', numBands2
   print 'fiducial3 bands:', numBands3

   if numBands == 3:
      blankSheet = cv2.cvtColor(blankSheetC, cv.CV_BGR2GRAY)
   elif numBands == 1:
      blankSheet = blankSheetC

   if numBands1 == 3:
      fiducial1 = cv2.cvtColor(fiducial1C, cv.CV_BGR2GRAY)
   elif numBands2 == 1:
      fiducial1 = fiducial1C

   if numBands2 == 3:
      fiducial2 = cv2.cvtColor(fiducial2C, cv.CV_BGR2GRAY)
   elif numBands2 == 1:
      fiducial2 = fiducial2C

   if numBands3 == 3:
      fiducial3 = cv2.cvtColor(fiducial3C, cv.CV_BGR2GRAY)
   elif numBands3 == 1:
      fiducial3 = fiducial3C

   freqFid1 = numpy.fft.fft2(fiducial3)
   freqBlank = numpy.fft.fft2(blankSheet)

   freqFid1 = numpy.fft.fftshift(freqFid1)
   freqBlank = numpy.fft.fftshift(freqBlank)

   magFid1 = numpy.absolute(freqFid1)
   magBlank = numpy.absolute(freqBlank)

   #Takes the log of the magnitude frequency image in order to diplay it
   logMagnitude = numpy.log10(magFid1)
   #Scales the image in order to display
   scaledIm = logMagnitude/numpy.max(logMagnitude)
   scaledIm2 = scaledIm * 255
   intScaledIm2 = scaledIm2.astype(numpy.uint8)
   cv2.namedWindow('fftFiducial', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('fftFiducial', intScaledIm2)
   cv2.waitKey()
   cv2.imwrite('fftFiducial.tif', intScaledIm2)

   #Takes the log of the magnitude frequency image in order to diplay it
   logMagnitude1 = numpy.log10(magBlank)
   #Scales the image in order to display
   scaledIm1 = logMagnitude/numpy.max(logMagnitude1)
   scaledIm21 = scaledIm1 * 255
   intScaledIm21 = scaledIm21.astype(numpy.uint8)
   cv2.namedWindow('fftBlank', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('fftBlank', intScaledIm21)
   cv2.waitKey()
   cv2.imwrite('fftBlank.tif', intScaledIm21)

   phaseFid1 = numpy.angle(freqFid1)
   phaseBlank = numpy.angle(freqBlank)

   correlation = magBlank * magFid1 * numpy.exp(1j * (phaseBlank - phaseFid1))
 
   corrSpat = numpy.fft.ifft2(correlation)
   corrSpat = numpy.absolute(numpy.fft.fftshift(corrSpat))

   dispCorrSpat = corrSpat / numpy.max(corrSpat)

   print dispCorrSpat.max(), dispCorrSpat.min()

   cv2.namedWindow('corrSpat', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('corrSpat', dispCorrSpat)
   cv2.waitKey()

   locationMax = numpy.argmax(corrSpat)
   rowLoc, colLoc = numpy.unravel_index(locationMax, (numRows, numCols))
   displayIm = cv2.merge((blankSheet, blankSheet, blankSheet))
   print rowLoc, colLoc

   displayIm[rowLoc - 2:rowLoc+3, colLoc-2:colLoc+3, 2] = 0
   displayIm[rowLoc-2:rowLoc+3, colLoc-2:colLoc+3, 0:1] = 255

   cv2.namedWindow('displayIm', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('displayIm', displayIm)
   cv2.waitKey()
   cv2.imwrite('dotsFid3.tif', displayIm)
   '''
   fftFid1 = numpy.fft.ifftshift(centerFreqFid1)
   fftBlank = numpy.fft.ifftshift(centerFreqBlank)
   Fid1 = numpy.fft.ifft2(fftFid1)
   Blank = numpy.fft.ifft2(fftBlank)
   '''
   return rowLoc, colLoc

if __name__ == '__main__':
   fiducial1C = cv2.imread('fiducial1.tif')
   fiducial2C = cv2.imread('fiducial2.tif')
   fiducial3C = cv2.imread('fiducial3.tif')
   blankSheetC = cv2.imread('original.tif')
   fftCorrelation(fiducial1C, fiducial2C, fiducial3C, blankSheetC)
