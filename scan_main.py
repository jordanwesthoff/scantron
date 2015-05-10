import ipcv 
import numpy
import cv2

def scan_main(pdf,original):
   answerSheets, blank = ipcv.read_in_files(pdf,original)
   numRows, numCols, numBands, dataType = ipcv.dimensions(answerSheets)
   numRowsO, numColsO, numBandsO, dataTypeO = ipcv.dimensions(blank)
   regIm = numpy.zeros((numRowsO, numColsO, numBands))
   
   for answer in range(answerSheets):
      fiducial1, fiducial2, fiducial3 = ipcv.paddingFiducials(answerSheets[:,:,answer], blank)

      #Find points for the centers of the fiducials in the answer sheets
      fid1row, fid1col = ipcv.fftCorrelation2(fid1,answerSheets[:,:,answer])
      fid2row, fid2col = ipcv.fftCorrelation2(fid2,answerSheets[:,:,answer])
      fid3row, fid3col = ipcv.fftCorrelation2(fid3,answerSheets[:,:,answer])
      

      #Answer Sheet is rotated 180 degrees
      numRowsIm, numColsIm, numBandsIm, dataTypeIm = ipcv.dimensions(answerSheets[:,:,answer])
      if fid2row - 25 < fid1row < fid2row + 25 and fid3col - 25 < fid2col < fid3col + 25 and fid2row < numRowsIm/2 and fid3col < numColsIm/2:
         answerSheets[:,:,answer] = numpy.rot90(answerSheets[answer], k=2)
         fid1row, fid1col = ipcv.fftCorrelation2(fid1, answerSheets[:,:,answer])
         fid2row, fid2col = ipcv.fftCorrelation2(fid2, answerSheets[:,:,answer])
         fid3row, fid3col = ipcv.fftCorrelation2(fid3, answerSheets[:,:,answer])

      #Rotate, translate, and Scale
      regIm[answer] = ipcv.register(fid1row, fid1col, fid2row, fid2col, fid3row, fid3col, answerSheets[:,:,answer], blank)

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
