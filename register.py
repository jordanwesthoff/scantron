import cv2
import numpy
import ipcv
#def register(fid1row, fid1col, fid2row, fid2col, fid3row, fid3col, blank1row, blank1col, blank2row, blank2col, blank3row, blank3col, image, blank):
def register(fid1, fid2, fid3, image, blank):
   numRows, numCols, numBands, dtype = ipcv.dimensions(blank)
   
   blank1row, blank1col = ipcv.fftCorrelation2(fid1,blank)
   blank2row, blank2col = ipcv.fftCorrelation2(fid2,blank)
   blank3row, blank3col = ipcv.fftCorrelation2(fid3,blank)

   print 'blank1row', blank1row
   print 'blank1col', blank1col
   print 'blank2row', blank2row
   print 'blank2col', blank2col
   print 'blank3row', blank3row
   print 'blank3col', blank3col
  

   #blankfid1 = numpy.array([738,60])
   #blankfid2 = numpy.array([738,542])
   #blankfid3 = numpy.array([53,556])
   
   #print blankfid2.shape

   fid1row, fid1col = ipcv.fftCorrelation2(fid1,image)
   fid2row, fid2col = ipcv.fftCorrelation2(fid2,image)
   fid3row, fid3col = ipcv.fftCorrelation2(fid3,image)

   print 'fid1row', fid1row
   print 'fid1col', fid1col
   print 'fid2row', fid2row
   print 'fid2col', fid2col
   print 'fid3row', fid3row
   print 'fid3col', fid3col
   
   numRowsIm, numColsIm, numBandsIm, dataTypeIm = ipcv.dimensions(image)
   
   #Rotated 180 degrees
   if fid2row - 25 < fid1row < fid2row + 25 and fid3col - 25 < fid2col < fid3col + 25 and fid2row < numRowsIm/2 and fid3col < numColsIm/2:
      print 'hello'
      image = numpy.rot90(image, k=2)
      cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
      cv2.imshow('image', image)
      fid1row, fid1col = ipcv.fftCorrelation2(fid1,image)
      fid2row, fid2col = ipcv.fftCorrelation2(fid2,image)
      fid3row, fid3col = ipcv.fftCorrelation2(fid3,image)
   
   
   blankpts = numpy.array([[blank1row,blank1col],[blank2row,blank2col],[blank3row,blank3col]]).astype(numpy.float32)
   #blankpts = numpy.array([blankfid1,blankfid2,blankfid3]).astype(numpy.float32)
   #print blankpts.shape
   fidpts = numpy.array([[fid1row,fid1col],[fid2row,fid2col],[fid3row,fid3col]]).astype(numpy.float32)
   #print fidpts.shape
   M = cv2.getAffineTransform(blankpts,fidpts)
   regIm = cv2.warpAffine(image,M,(numCols,numRows), borderMode = cv2.BORDER_TRANSPARENT)
   
   cv2.namedWindow('rot',cv2.WINDOW_AUTOSIZE)
   cv2.imshow('rot',regIm.astype(numpy.uint8))
   cv2.waitKey()

   cv2.imwrite('new0001.tif', regIm.astype(numpy.uint8))

   return regIm
if __name__ == '__main__':
   import cv2
   fid1 = 'fiducial1.tif'
   fid2 = 'fiducial2.tif'
   fid3 = 'fiducial3.tif'
   #image = 'test0002rot.tif'
   image = 'reference0001.tif'
   image2 = 'test0004.tif'
   image3 = 'test0000.tif'
   image4 = 'test0008.tif'
   blank = 'original.tif'
  
   fid1 = cv2.imread(fid1)
   fid2 = cv2.imread(fid2)
   fid3 = cv2.imread(fid3)
   image = cv2.imread(image)
   cv2.namedWindow('blank', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('blank', image)
   cv2.waitKey()
   
   #image = numpy.rot90(image, k=2)
   #cv2.imwrite('180degrees.tif', image)
   blank = cv2.imread(blank)
   cv2.namedWindow('blank', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('blank', blank)
   cv2.waitKey()
   image2 = cv2.imread(image2)
   image3 = cv2.imread(image3)
   image4 = cv2.imread(image4)
   #print numpy.average(image), numpy.average(image2), numpy.average(image3), numpy.average(image4)
   regIm = ipcv.register(fid1, fid2, fid3, image, blank)
   #regIm = ipcv.register(fid1row, fid1col, fid2row, fid2col, fid3row, fid3col, blank1row, blank1col, blank2row, blank2col, blank3row, blank3col, image, blank)








