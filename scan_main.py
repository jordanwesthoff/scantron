import ipcv 
import numpy
import cv2

def scan_main(pdf,original):
   answerSheets, blankSheet1 = ipcv.read_in_files(pdf,original)
   numRowsO, numColsO, numBandsO, dataTypeO = ipcv.dimensions(blankSheet1)
   regIm = numpy.zeros((numRowsO,numColsO,len(answerSheets)))
   for answer in range(len(answerSheets)):
      answerSheet1 = numpy.asarray(answerSheets[answer])
      blankSheet1 = numpy.asarray(blankSheet1)

      answerSheet = answerSheet1
      blankSheet = blankSheet1

      fiducial1  = ipcv.paddingFid1(answerSheet, blankSheet)
      fiducial2  = ipcv.paddingFid2(answerSheet, blankSheet)
      fiducial3  = ipcv.paddingFid3(answerSheet, blankSheet)
      
      #Find points for the centers of the fiducials in the blank sheets
      blank1row, blank1col = ipcv.fftCorrelation2(fiducial1,blankSheet)
      blank2row, blank2col = ipcv.fftCorrelation2(fiducial2,blankSheet)
      blank3row, blank3col = ipcv.fftCorrelation2(fiducial3,blankSheet)

      #Find points for the centers of the fiducials in the answer sheets
      fid1row, fid1col = ipcv.fftCorrelation2(fiducial1,answerSheet)
      fid2row, fid2col = ipcv.fftCorrelation2(fiducial2,answerSheet)
      fid3row, fid3col = ipcv.fftCorrelation2(fiducial3,answerSheet)
     
      #Rotate, translate, and Scale
      regIm[:,:,answer] = ipcv.register(fid1row, fid1col, fid2row, fid2col, fid3row, fid3col, blank1row, blank1col, blank2row, blank2col, blank3row, blank3col, answerSheet, blankSheet)

      #Grading
   return regIm

if __name__ == '__main__':
   import numpy
   import cv2
   import time
   pdf = 'answer_sheets.pdf'
   original = 'original.pdf'
   startTime = time.clock()
   results = ipcv.scan_main(pdf, original)
   elapsedTime = time.clock() - startTime
   print 'elapsedTime:', elapsedTime, 'sec'
   cv2.namedWindow('registeredIm', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('registeredIm', results[:,:,3].astype(numpy.uint8))
   cv2.waitKey()

   action = ipcv.flush()
