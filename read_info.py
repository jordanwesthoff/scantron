import ipcv
import numpy
import cv2
import cv

def read_info(sheets, original):
#   original = cv2.cvtColor(original,cv.CV_BGR2GRAY)
#   sheets = cv2.cvtColor(sheets,cv.CV_BGR2GRAY)
   hood = numpy.ones((12,12))
   numRows, numCols, numBands, dtype = ipcv.dimensions(original)
#   original = numpy.absolute(original - sheets)
#   cv2.namedWindow('orig',cv2.WINDOW_AUTOSIZE)
#   cv2.imshow('orig', original)
#   cv2.waitKey()
   lastName = []
   hcol = 12
   hrow = 12 
   col = 72
 #  col =162 
   cv2.namedWindow('hood')
   letter = numpy.zeros((26,1))
   for C in range(11):
      row = 51
      for L  in range(26):
         hood = original[row:row + hrow,col:col +hcol]
       #  print 'hood', numpy.mean(hood)
        # if numpy.mean(hood) < 180:
 #        im,threshold = ipcv.otsu_threshold(hood,255, verbose=False)
         #print 'thresh', threshold
         if numpy.mean(hood) < 185:
            total = 0
         else:
            total = 255
        # print 'total', total
#         total = numpy.sum(hood)
         letter[L] = total
         row = row +hrow
         if L == 6:
            row = row-1
       #  print 'row',row
         cv2.imshow('hood',hood)
         cv2.waitKey(600)
      val = (letter[numpy.argmin(letter)])
      #val = (letter[numpy.argmin(letter)])
      print 'lastval',val
      mean = numpy.mean(letter)
      print 'mean', mean
      #if mean - 1 < val < mean + 1:
      if val > 0:
      #if mean - 9000 < val < mean + 9000:
    #  if mean - 5900 < val < mean + 5900:
         lastName.append(chr(32))
         
      else:
         lastName.append(chr(numpy.argmin(letter)+65))
      col = col + hcol 
   print 'lastname',lastName
   '''
   hood = numpy.ones((9,10))
   numRows, numCols, numBands, dtype = ipcv.dimensions(original)
#   original = numpy.absolute(original - sheets)
#   cv2.namedWindow('orig',cv2.WINDOW_AUTOSIZE)
#   cv2.imshow('orig', original)
#   cv2.waitKey()
   lastName = []
   drow = 3
   dcol = 2
   hcol = 10
   hrow = 9
  # col = 72
   col =162 
   cv2.namedWindow('hood')
   letter = numpy.zeros((26,1))
   for C in range(11):
      row = 51
      for L  in range(26):
         hood = original[row:row + hrow,col:col +hcol]
       #  print 'hood', numpy.mean(hood)
        # if numpy.mean(hood) < 180:
 #        im,threshold = ipcv.otsu_threshold(hood,255, verbose=False)
         #print 'thresh', threshold
#         if numpy.mean(hood) < threshold:
#            total = 0
#         else:
#            total = 255
         total = numpy.sum(hood)
         letter[L] = total
         row = row + drow +hrow
         if L == 6:
            row = row-1
       #  print 'row',row
       #  cv2.imshow('hood',hood)
       #  cv2.waitKey(600)
      val = (letter[numpy.argmin(letter)])
      val = (letter[numpy.argmin(letter)])
      print 'lastval',val
      mean = numpy.mean(letter)
      print 'mean', mean
     # if mean - 3 < val < mean + 3:
      #if mean - 9000 < val < mean + 9000:
      if mean - 5900 < val < mean + 5900:
         lastName.append(chr(32))
         
      else:
         lastName.append(chr(numpy.argmin(letter)+65))
      col = col + hcol + dcol
   print 'lastname',lastName
  # print 'letter', letter
  # print 'row',row
  # print 'col',col
   

   firstName = [] 
   drow = 3
   dcol = 2
   hcol = 10
   hrow = 9
   col = 235
   cv2.namedWindow('hood')
   letter = numpy.zeros((26,1))
   for C in range(9):
      row = 51
      for L  in range(26):
         hood = original[row:row + hrow,col:col +hcol]
         total = numpy.sum(hood)
         letter[L] = total
         row = row + drow +hrow
         if L == 6:
            row = row-1
      val = (letter[numpy.argmin(letter)])
      mean = numpy.mean(letter)
      if mean - 9000 < val < mean + 9000:
         firstName.append(chr(32))
         
      else:
         firstName.append(chr(numpy.argmin(letter)+65))
     # firstName[C] = numpy.argmax(letter)
      col = col + hcol + dcol
   print 'firstname',firstName
   
   
  # UID = numpy.zeros((9))
   UID = []
   drow = 3
   dcol = 2
   hcol = 10
   hrow = 9
   col = 370
   cv2.namedWindow('hood')
   letter = numpy.zeros((10,1))
   for C in range(9):
      row = 51
      for L  in range(10):
         hood = original[row:row + hrow,col:col +hcol]
         total = numpy.sum(hood)
         letter[L] = total
         row = row + drow +hrow
         if L == 6:
            row = row-1
      mean = numpy.mean(letter)
      val = (letter[numpy.argmin(letter)])
      if mean - 9000 < val < mean + 9000:
         UID.append(chr(32))
      else:
         UID.append(numpy.argmin(letter))
     # UID[C] = numpy.argmax(letter)
      col = col + hcol + dcol
   
   print 'UID',UID
   
   #additional = numpy.zeros((9))
   additional = []
   drow = 3
   dcol = 2
   hcol = 10
   hrow = 9
   col = 370
   cv2.namedWindow('hood')
   letter = numpy.zeros((10,1))
   for C in range(9):
      row = 218
      for L  in range(10):
         hood = original[row:row + hrow,col:col +hcol]
         total = numpy.sum(hood)
         letter[L] = total
         row = row + drow +hrow
        # if L == 6:
        #    row = row-1
      mean = numpy.mean(letter)
      val = (letter[numpy.argmin(letter)])
      if mean - 8000 < val < mean + 8000:
         UID.append(chr(32))
      else:
         additional.append(numpy.argmin(letter))
     # additional[C] = numpy.argmax(letter)
      col = col + hcol + dcol
   print 'add', additional

   return lastName,firstName,UID,additional
   '''
if __name__ == '__main__':
   
   import cv2
   import ipcv
 #  import scantron
#   filename = 'reg0000.tif'
#   filename = 'reg0002.tif'
#   filename = 'rot0000.tif'
#   filename = 'rot0001.tif'
#   filename = 'rot0002.tif'
#   filename = 'rot0003.tif'
#   filename = 'rot0004.tif'
#   filename = 'rot0005.tif'
#   filename = 'rot0006.tif'
   filename = 'rot0007.tif'
#   filename = 'rot0008.tif'
  # filename = 'answer_sheets.pdf'
  # blank = 'original.tif'
   blank = 'paddedBlank.tif'
  # blank = 'original_scan_sheets.pdf'
#   sheets,original = ipcv.scantron.read_in_files(filename, blank)
   original = cv2.imread(filename)
  # original = cv2.imread(blank)
   sheets = cv2.imread(blank)
   test = read_info(sheets,original)

