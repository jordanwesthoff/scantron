import ipcv
import numpy
import cv2

def read_info(sheets, original):
   hood = numpy.ones((9,10))
   numRows, numCols, numBands, dtype = ipcv.dimensions(original)
   
   lastName = numpy.zeros((11))
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
      lastName[C] = numpy.argmax(letter)
      col = col + hcol + dcol
  # print 'letter', letter
  # print 'row',row
  # print 'col',col
   
   
   firstName = numpy.zeros((9))
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
      firstName[C] = numpy.argmax(letter)
      col = col + hcol + dcol
   
   
   UID = numpy.zeros((9))
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
      UID[C] = numpy.argmax(letter)
      col = col + hcol + dcol
   

   additional = numpy.zeros((9))
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
      additional[C] = numpy.argmax(letter)
      col = col + hcol + dcol

   return lastName,firstName,UID,additional

if __name__ == '__main__':
   
   import cv2
   import ipcv
 #  import scantron
   filename = 'answer_sheets.pdf'
   blank = 'original_scan_sheets.pdf'
   sheets,original = ipcv.scantron.read_in_files(filename, blank)
   test = read_info(sheets,original)

