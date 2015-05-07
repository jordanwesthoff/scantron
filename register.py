import cv2
import numpy
import ipcv

def register(fid1,fid2,fid3,image):
   
   blankfid1 = numpy.array([738,60])
   blankfid2 = numpy.array([738,542])
   blankfid3 = numpy.array([53,556])
   print blankfid2.shape

   fid1row, fid1col = ipcv.fftCorrelation2(fid1,image)
   fid2row, fid2col = ipcv.fftCorrelation2(fid2,image)
   fid3row, fid3col = ipcv.fftCorrelation2(fid3,image)
   
   blankpts = numpy.array([blankfid1,blankfid2,blankfid3]).astype(numpy.float32)
   print blankpts.shape
   fidpts = numpy.array([[fid1row,fid1col],[fid2row,fid2col],[fid3row,fid3col]]).astype(numpy.float32)
   print fidpts.shape
   M = cv2.getAffineTransform(blankpts,fidpts)
   

if __name__ == '__main__':
   import cv2
   fid1 = 'fiducial1.tif'
   fid2 = 'fiducial2.tif'
   fid3 = 'fiducial3.tif'
   image = 'test0000.tif'
   
   fid1 = cv2.imread(fid1)
   fid2 = cv2.imread(fid2)
   fid3 = cv2.imread(fid3)
   image = cv2.imread(image)
   regIM = ipcv.register(fid1,fid2,fid3,image)








