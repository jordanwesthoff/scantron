import ipcv
import numpy
import cv2

def read_info(sheets, original):
   hood = numpy.ones((9,10))
   numRows, numCols, numBands, dtype = ipcv.dimensions(original)
   
   lastName = []
   drow = 3
   dcol = 2
   hcol = 10
   hrow = 9
   col = 72
   cv2.namedWindow('hood')
   letter = numpy.zeros((26,1))
   for C in range(11):
      row = 51
      for L  in range(26):
         hood = original[row:row + hrow,col:col +hcol]
         total = numpy.sum(hood)
         letter[L] = total
         row = row + drow +hrow
         if L == 6:
            row = row-1
       #  print 'row',row
       #  cv2.imshow('hood',hood)
       #  cv2.waitKey(600)
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
   
if __name__ == '__main__':
   
   import cv2
   import ipcv
 #  import scantron
   filename = 'rot0003.tif'
  # filename = 'rot0001.tif'
  # filename = 'answer_sheets.pdf'
   blank = 'original.tif'
  # blank = 'original_scan_sheets.pdf'
#   sheets,original = ipcv.scantron.read_in_files(filename, blank)
   original = cv2.imread(filename)
   sheets = cv2.imread(blank)
   test = read_info(sheets,original)

