import cv2 
import os
import glob
#import scantron 
import ipcv
import cv
import numpy

def read_in_files2(pdf,blank):

   #convert pdf to tif
  # os.system( "convert " + pdf + " answers_%d.tif")
  # os.system( "convert " + blank + " orig.tif")
   original = cv2.imread('original_300.tif')
   numR, numC, numB, dtype = ipcv.dimensions(original)
   print original.shape
   if numB ==3:
      original = cv2.cvtColor(original,cv.CV_BGR2GRAY)
   
   original[original<=200]=0
   original[original>200]=255
   print original.shape
   cv2.imwrite('original300dpi.tif',original )
   lis = glob.glob('answers_rot*.tif')
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
      if numpy.average(im) > 230:
         im[im<=200]=0
         im[im>200]=255
         cv2.imwrite('blackDPI%04i.tif' %count,im)
      else:
         cv2.imwrite('blackDPI%04i.tif' %count,im)
      sheets.append(im)
      count = count +1
   return sheets, original
   
if __name__ == '__main__':

   filename = 'answer_sheets.pdf'
   blank = 'original_scan_sheet.pdf'
   im = read_in_files2(filename,blank)
