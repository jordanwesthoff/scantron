import ipcv
import numpy
import cv
import cv2

def grading(scantron): 

   numberRows, numberColumns, numberBands, dataType = ipcv.dimensions(scantron)
   
   neighborhood = numpy.zeros((12, 12))

   #For questions 1-25 (first column)
   column = 72
   newIm = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm[row : row + 12, column : column + 12] = 0
	 else:
	    newIm[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12  

   #For questions 26-50 (second column) 
   column = 148
   newIm = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm[row : row + 12, column : column + 12] = 0
	 else:
	    newIm[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12 	     
	      
   #For questions 51-75 (third column) 
   column = 225
   newIm = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm[row : row + 12, column : column + 12] = 0
	 else:
	    newIm[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12    
      
   #For questions 76-100 (fourth column) 
   column = 305
   newIm = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm[row : row + 12, column : column + 12] = 0
	 else:
	    newIm[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12   
      
   #For questions 101-125 (fifth column) 
   column = 385
   newIm = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm[row : row + 12, column : column + 12] = 0
	 else:
	    newIm[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12     
      
   #For questions 125-150 (last column) 
   column = 465
   newIm = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm[row : row + 12, column : column + 12] = 0
	 else:
	    newIm[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12       
   return newIm

def answers(key):      
   #ANSWER KEY

   numberRows, numberColumns, numberBands, dataType = ipcv.dimensions(key)
   
   neighborhood = numpy.zeros((12, 12))

   #For questions 1-25 (first column)
   column = 72
   newIm2 = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12  

   #For questions 26-50 (second column) 
   column = 148
   newIm2 = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12 	     
	      
   #For questions 51-75 (third column) 
   column = 225
   newIm2 = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12    
      
   #For questions 76-100 (fourth column) 
   column = 305
   newIm2 = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12   
      
   #For questions 101-125 (fifth column) 
   column = 385
   newIm2 = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12     
      
   #For questions 125-150 (last column) 
   column = 465
   newIm2 = scantron
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = scantron[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 155:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12      
   return newIm2
 
def subtraction(newIm, newIm2):      
   #subtracting images
   subtracted = newIm - newIm2
   subtracted = (255 - subtracted) / 255
   """numberRows, numberColumns, numberBands, dataType = ipcv.dimensions(subtracted)
   for row in range(numberRows):
      for column in range(numberColumns):
         if subtracted[row, column] == 0:
	    subtracted[row, column] = 255
	 if subtracted[row, column] == 255:
	    subtracted[row, column] = 0"""
  
   return subtracted



if __name__ == '__main__':

   import ipcv
   import ipcv
   import cv2
   
   filename = 'gray0001.tif'
   
   scantron = cv2.imread(filename, cv2.CV_LOAD_IMAGE_UNCHANGED)
   cv2.namedWindow('filename', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('filename', scantron)
   #cv2.waitKey()
   
   key = cv2.imread(filename, cv2.CV_LOAD_IMAGE_UNCHANGED)
   cv2.namedWindow('key', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('key', key)
   #cv2.waitKey()
   newIm = grading(scantron)
   newIm2 = answers(key)
   subtracted = subtraction(newIm, newIm2)

   cv2.namedWindow('subtracted', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('subtracted', subtracted)
   cv2.waitKey()
   
   cv2.namedWindow('graded', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('graded', newIm)
   cv2.waitKey()
