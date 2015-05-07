import cv2
import numpy
import ipcv
def fftCorrelation(fiducial1, fiducial2, fiducial3, blankSheet):
   
   numRows, numCols, numBands, dataType = ipcv.dimensions(blankSheet)
   numRows1, numCols1, numBands1, dataType1 = ipcv.dimensions(fiducial1)
   numRows2, numCols2, numBands2, dataType2 = ipcv.dimensions(fiducial2)
   numRows3, numCols3, numBands3, dataType3 = ipcv.dimensions(fiducial3)
   print 'blank bands:', numBands
   print 'fiducial1 bands:', numBands1
   print 'fiducial2 bands:', numBands2
   print 'fiducial3 bands:', numBands3
   freqFid1 = numpy.fft.fft2(fiducial1)
   freqBlank = numpy.fft.fft2(blankSheet)

   centerFreqFid1 = numpy.fft.fftshift(freqFid1)
   centerFreqBlank = numpy.fft.fftshift(freqBlank)

   magFid1 = numpy.abs(centerFreqFid1)
   magBlank = numpy.abs(centerFreqBlank)

   phaseFid1 = numpy.angle(centerFreqFid1, deg=0)
   phaseBlank = numpy.angle(centerFreqBlank, deg=0)

   correlation = magFid1 * magBlank * numpy.exp(-1 * (phaseFid1 - phaseBlank))
   print correlation.shape 
if __name__ == '__main__':
   fiducial1 = cv2.imread('fiducial1.tif')
   fiducial2 = cv2.imread('fiducial2.tif')
   fiducial3 = cv2.imread('fiducial3.tif')
   blankSheet = cv2.imread('original.tif')
   fftCorrelation(fiducial1, fiducial2, fiducial3, blankSheet)
