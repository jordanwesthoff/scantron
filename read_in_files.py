import cv2 
import os
import glob
#import scantron 
import ipcv
import cv

def read_in_files(pdf):
   #os.system( 'convert answer_sheets.pdf answers_%d.tif')

   #convert pdf to tif
  # os.system( "convert " + pdf + " answers_%d.tif")
   lis = glob.glob('*.tif')
   lis = sorted(lis)
   print'lis', lis
   count = 0
   sheets = []
   for im in range(len(lis) ):
      current = lis[im]
      current = cv2.imread(current)
#      numRows, numCols, numBands, dtype = scantron.dimensions(current)
      numRows, numCols, numBands, dtype = ipcv.dimensions(current)
      if numBands ==3:
         im = cv2.cvtColor(current,cv.CV_BGR2GRAY)
      else:
         im = current
      im[im<=200]=0
      im[im>200]=255
#      cv2.imwrite('gray%04i.tif' %count,im)
      sheets.append(im)
      count = count +1
   return sheets
   
if __name__ == '__main__':

   filename = 'answer_sheets.pdf'
   im = read_in_files(filename)
