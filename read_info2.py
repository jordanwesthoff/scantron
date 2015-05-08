import ipcv
import numpy
import cv2

def read_info2(sheets, original):
   hood = numpy.ones((39,37))
   numRows, numCols, numBands, dtype = ipcv.dimensions(original)
  # original = ((original*1.0) - (sheets*1.0)) *255
   original = ((original*1.0) - (sheets*1.0)) *255
  # original = original.astype(numpy.unit8)
  # cv2.namedWindow('orig',cv2.WINDOW_AUTOSIZE)
  # cv2.imshow('orig', original)
  # cv2.waitKey()
   
   lastName = []
   drow = 11 
   dcol = 13
   hcol = 37
   hrow = 39
   col = 303 
   cv2.namedWindow('hood')
   letter = numpy.zeros((26,1))
   for C in range(11):
      row = 211
      for L  in range(26):
         hood = original[row:row + hrow,col:col +hcol]
         total = numpy.sum(hood)
         letter[L] = total
         row = row + drow +hrow
         if L == 1 or L == 6 or L == 12 or L ==17 or L == 23:
            row = row-1
         print 'row',row
         cv2.imshow('hood',hood)
         cv2.waitKey(600)
      val = (letter[numpy.argmin(letter)])
      print 'lastval',val
      mean = numpy.mean(letter)
      print 'mean',mean
     # if mean - 3 < val < mean + 3:
     #    lastName.append(chr(32))
      if mean - 9000 < val < mean + 9000:
         lastName.append(chr(32))
         
      else:
         lastName.append(chr(numpy.argmin(letter)+65))
      col = col + hcol + dcol
   print 'lastname',lastName
  # print 'letter', letter
  # print 'row',row
  # print 'col',col
   
   firstName = [] 
   drow = 11
   dcol = 13
   hcol = 37
   hrow = 39
   col = 983
   cv2.namedWindow('hood')
   letter = numpy.zeros((26,1))
   for C in range(9):
      row = 211
      for L  in range(26):
         hood = original[row:row + hrow,col:col +hcol]
         total = numpy.sum(hood)
         letter[L] = total
         row = row + drow +hrow
        # if L == 6:
         if L == 1 or L == 6 or L == 12 or L ==17 or L == 23:
            row = row-1
         print 'row',row
         cv2.imshow('hood',hood)
         cv2.waitKey(300)
      val = (letter[numpy.argmin(letter)])
      mean = numpy.mean(letter)
      if mean - 9000 < val < mean + 9000:
         firstName.append(chr(32))
         
      else:
         firstName.append(chr(numpy.argmin(letter)+65))
     # firstName[C] = numpy.argmax(letter)
      col = col + hcol + dcol
   print 'firstname',firstName
   
   '''
   '''
  # UID = numpy.zeros((9))
   UID = []
   drow = 11
   dcol = 13
   hcol = 37
   hrow = 39
   col = 1545 
   cv2.namedWindow('hood')
   letter = numpy.zeros((10,1))
   for C in range(9):
      row = 211
      for L  in range(10):
         hood = original[row:row + hrow,col:col +hcol]
         total = numpy.sum(hood)
         letter[L] = total
         row = row + drow +hrow
        # if L == 6:
         if L == 1 or L == 6 or L == 12 or L ==17 or L == 23:
            row = row-1
         print 'row',row
         cv2.imshow('hood',hood)
         cv2.waitKey(300)
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
   drow = 11 
   dcol = 13
   hcol = 37
   hrow = 39
   col = 1545
   cv2.namedWindow('hood')
   letter = numpy.zeros((10,1))
   for C in range(9):
      row = 907
      for L  in range(10):
         hood = original[row:row + hrow,col:col +hcol]
         total = numpy.sum(hood)
         letter[L] = total
         row = row + drow +hrow
         if L == 3 or L == 8:
            row = row-1
         print 'row',row
         cv2.imshow('hood',hood)
         cv2.waitKey(300)
      mean = numpy.mean(letter)
      val = (letter[numpy.argmin(letter)])
      if mean - 8000 < val < mean + 8000:
         additional.append(chr(32))
      else:
         additional.append(numpy.argmin(letter))
     # additional[C] = numpy.argmax(letter)
      col = col + hcol + dcol
   print 'add', additional

   return lastName,firstName,UID,additional
    
if __name__ == '__main__':
   
   import cv2
   import ipcv
 #  import scantron
  # filename = 'answers_rot0.tif'
  # filename = 'answers_rot1.tif'
  # filename = 'answers_rot2.tif'
  # filename = 'answers_rot3.tif'
  # filename = 'answers_rot4.tif'
   filename = 'answer_sheets.pdf'
   blank = 'original300dpi.tif'
  # blank = 'original_scan_sheets.pdf'
#   sheets,original = ipcv.scantron.read_in_files(filename, blank)
   sheets = cv2.imread(filename)
   original  = cv2.imread(blank)
   test = read_info2(sheets,original)

