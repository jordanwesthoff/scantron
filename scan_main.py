import ipcv 
import numpy
import cv2

def scan_main(pdf,original):
   answerSheets, blankSheet1 = ipcv.read_in_files(pdf,original)
   print len(answerSheets)
   for answer in range(len(answerSheets)):
      answerSheet1 = numpy.asarray(answerSheets[answer])
      blankSheet1 = numpy.asarray(blankSheet1)
      print blankSheet1
      fiducial1, fiducial2, fiducial3, answerSheet, blankSheet = ipcv.paddingFiducials(answerSheet1, blankSheet1)

      #Find points for the centers of the fiducials in the blank sheets
      blank1row, blank1col = ipcv.fftCorrelation2(fiducial1,blankSheet)
      blank2row, blank2col = ipcv.fftCorrelation2(fiducial2,blankSheet)
      blank3row, blank3col = ipcv.fftCorrelation2(fiducial3,blankSheet)

      #Find points for the centers of the fiducials in the answer sheets
      fid1row, fid1col = ipcv.fftCorrelation2(fid1,answerSheet)
      fid2row, fid2col = ipcv.fftCorrelation2(fid2,answerSheet)
      fid3row, fid3col = ipcv.fftCorrelation2(fid3,answerSheet)
      
      #Rotate, translate, and Scale
      regIm = ipcv.register(fid1row, fid1col, fid2row, fid2col, fid3row, fid3col, blank1row, blank1col, blank2row, blank2col, blank3row, blank3col, answerSheets[answer], blankSheet)

      #Grading
      return regIm

if __name__ == '__main__':
   import numpy
   import cv2
   pdf = 'answer_sheets.pdf'
   original = 'original.pdf'
   results = ipcv.scan_main(pdf,original)
   cv2.namedWindow('registeredIm', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('registeredIm', results[:,:,1])
