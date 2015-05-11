import ipcv
import numpy
import cv
import cv2
import matplotlib.pyplot

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
         if numpy.mean(neighborhood) < 190:
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
         if numpy.mean(neighborhood) < 190:
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
         if numpy.mean(neighborhood) < 190:
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
         if numpy.mean(neighborhood) < 190:
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
         if numpy.mean(neighborhood) < 190:
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
         if numpy.mean(neighborhood) < 190:
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
   newIm2 = key
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = key[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 190:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12  

   #For questions 26-50 (second column) 
   column = 148
   newIm2 = key
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = key[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 190:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12 	     
	      
   #For questions 51-75 (third column) 
   column = 225
   newIm2 = key
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = key[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 190:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12    
      
   #For questions 76-100 (fourth column) 
   column = 305
   newIm2 = key
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = key[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 190:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12   
      
   #For questions 101-125 (fifth column) 
   column = 385
   newIm2 = key
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = key[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 190:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12     
      
   #For questions 125-150 (last column) 
   column = 465
   newIm2 = key
   for answer in range(5): 
      row = 385 
      for question in range(25):
         neighborhood = key[row : row + 12, column : column + 12]
         if numpy.mean(neighborhood) < 190:
	    newIm2[row : row + 12, column : column + 12] = 0
	 else:
	    newIm2[row : row + 12, column : column + 12] = 255
         row = row + 12
      column = column + 12      
   return newIm2
 
def subtraction(newIm, newIm2):      
   #subtracting images
   subtracted = numpy.abs(newIm2 - newIm)
   subtracted = (255 - subtracted)
   numberRows, numberColumns, numberBands, dataType = ipcv.dimensions(subtracted)
  
   return subtracted

def convolution(subtracted, threshold = .9): 
   numberRows, numberColumns, numberBands, dataType = ipcv.dimensions(subtracted)

   answerRegion = numpy.zeros((300, 60))
   kernel = numpy.zeros((12,12))
   neighborhood = numpy.ones((12, 60))
     
   answerRegion = answerRegion * 1.0
   kernel = kernel * 1.0
   
   answerRegion = subtracted[numberRows-407:numberRows-107, numberColumns-540:numberColumns-480]
   cv2.imshow('region', answerRegion)
   
   numberRowsR, numberColumnsR, numberBandsR, dataType = ipcv.dimensions(answerRegion)
   
   if numberBandsR == 3:
      answerRegion = cv2.cvtColor(answerRegion,cv.CV_BGR2GRAY)

   answerRegion[answerRegion <= 200] = 0
   answerRegion[answerRegion > 200] = 255
   
   count = 0
   #cv2.namedWindow('hood', cv2.WINDOW_AUTOSIZE)
   #for row in range(numberRowsR):
   for row in range(25):
      row = row * 12
      neighborhood = answerRegion[row : row + 12, 0:numberColumnsR]
      #cv2.imshow('hood', neighborhood)
      #cv2.waitKey(300)
      print neighborhood.shape
      if numpy.mean(neighborhood) >= 254:
	 count = count + 1
         print count
      else:
         count = count + 0
      row = row + 12           
   print count
   count1 = count
   
   #column 2
   answerRegion = subtracted[numberRows-407:numberRows-107, numberColumns-464:numberColumns-404]
   cv2.imshow('region', answerRegion)
   cv2.waitKey()
   
   numberRowsR, numberColumnsR, numberBandsR, dataType = ipcv.dimensions(answerRegion)
   
   if numberBandsR == 3:
      answerRegion = cv2.cvtColor(answerRegion,cv.CV_BGR2GRAY)

   answerRegion[answerRegion <= 200] = 0
   answerRegion[answerRegion > 200] = 255
   
   count = 0
   #cv2.namedWindow('hood', cv2.WINDOW_AUTOSIZE)
   for row in range(25):
      row = row * 12
      neighborhood = answerRegion[row : row + 12, 0:numberColumnsR]
      #cv2.imshow('hood', neighborhood)
      #cv2.waitKey(300)
      print neighborhood.shape
      if numpy.mean(neighborhood) >= 254:
	 count = count + 1
         print count
      else:
         count = count + 0
      row = row + 12          
   print count
   count2 = count
   
   count = count1 + count2 
   print count
   
   return count    
   
def finalGrade(count):
   
   numberQuestions = 25 * 1.0 
   numberRight = count * 1.0
   print numberRight 
   
   percent = (numberRight / numberQuestions) * 100
   
   print percent
   return percent

if __name__ == '__main__':

   import ipcv
   import ipcv
   import cv2
   
   key = 'rot0000.tif'
   scantron = 'rot0001.tif' 
   
   scantron = cv2.imread(scantron, cv2.CV_LOAD_IMAGE_UNCHANGED)
   #cv2.namedWindow('filename', cv2.WINDOW_AUTOSIZE)
   #cv2.imshow('filename', scantron)
   #cv2.waitKey()
   
   key = cv2.imread(key, cv2.CV_LOAD_IMAGE_UNCHANGED)
   #cv2.namedWindow('key', cv2.WINDOW_AUTOSIZE)
   #cv2.imshow('key', key)
   #cv2.waitKey()
   
   newIm = grading(scantron)
   newIm2 = answers(key)
   subtracted = subtraction(newIm, newIm2)
   count = convolution(subtracted, threshold = .9)
   percent = finalGrade(count)

   #cv2.namedWindow('subtracted', cv2.WINDOW_AUTOSIZE)
   #cv2.imshow('subtracted', subtracted)
   #cv2.waitKey()
   #cv2.imwrite('subtracted.tif', subtracted)
   
   #cv2.namedWindow('gradedKey', cv2.WINDOW_AUTOSIZE)
   #cv2.imshow('gradedKey', newIm)
   #cv2.waitKey()
   #cv2.imwrite('gradedKey.tif', newIm)
     
   #cv2.namedWindow('graded', cv2.WINDOW_AUTOSIZE)
   #cv2.imshow('graded', newIm2)
   #cv2.waitKey()
   #cv2.imwrite('graded.tif', newIm2)"""

   """# Display the results to the user
   maximum = numpy.amax(histogram) + 1
   matplotlib.pyplot.figure()
   matplotlib.pyplot.xlabel('choice')
   matplotlib.pyplot.ylabel('Count')  
   matplotlib.pyplot.xlim([0, len(histogram)])
   matplotlib.pyplot.ylim([0, maximum])
   matplotlib.pyplot.plot(histogram, color='b')
   matplotlib.pyplot.suptitle('Number of wrong answers', fontsize=14, fontweight='bold')
   matplotlib.pyplot.show()"""
