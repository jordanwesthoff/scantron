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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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
         if numpy.mean(neighborhood) < 185:
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

def convolution(subtracted, threshold = .000001): 
   numberRows, numberColumns, numberBands, dataType = ipcv.dimensions(subtracted)
   response = numpy.zeros((numberRows, numberColumns))
   numIncorrect = numpy.zeros((numberRows, numberColumns))
   #histogram = numpy.zeros((25,1))
   box = numpy.zeros((12, 12))

   subtracted = cv2.cvtColor(subtracted, cv.CV_BGR2GRAY)   
   subtracted[subtracted <= 200] = 0
   subtracted[subtracted > 200] = 255
   subtracted[0:380, :] = 255
   cv2.namedWindow('subtracted', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('subtracted', subtracted)
   cv2.waitKey()
   #
   cv2.imwrite('subtractedIm.tif', subtracted)

   box = box * 1.0 
   subtracted = subtracted * 1.0 
   
   maxCount = numpy.max(subtracted)
   
   subtracted = (maxCount - subtracted) / maxCount
   box = (maxCount - box) / maxCount
   print 'box', box
	 
   #applying 2D filter
   #For questions 1-25 (first column)
   #for row in range(numberRows):
      #for column in range(numberColumns):
         #if row < 385 or column < 72:
	    #response = 0
            #print 'response before:', response
	 #else:
   response = cv2.filter2D(subtracted, -1, box)
   print 'response after:', response
   #if response is less than the threshold, a match does not occur    	  
   numIncorrect[response < threshold] = 0
   #if response is greater than/equal to the threshold, a match occurs
   numIncorrect[response >= threshold] = 1
   print numIncorrect
   totalIncorrect = numpy.sum(numIncorrect)
   print 'totalIncorrect', totalIncorrect    
   """response = (cv2.filter2D(subtracted, -1, box))
   print numpy.max(response)       
   #if response is less than threshold a match does not occur
   numIncorrect[response < threshold] = 0
   #if response is greater than/equal to the threshold, a match occurs
   numIncorrect[response >= threshold] = 1
   histogram = numpy.sum(numIncorrect) 
   print histogram"""
   return numIncorrect    


if __name__ == '__main__':

   import ipcv
   import ipcv
   import cv2
   
   key = 'rot0007.tif'
   scantron = 'rot0008.tif' 
   
   scantron = cv2.imread(scantron, cv2.CV_LOAD_IMAGE_UNCHANGED)
   cv2.namedWindow('filename', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('filename', scantron)
   #cv2.waitKey()
   
   key = cv2.imread(key, cv2.CV_LOAD_IMAGE_UNCHANGED)
   cv2.namedWindow('key', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('key', key)
   #cv2.waitKey()
   
   newIm = grading(scantron)
   newIm2 = answers(key)
   subtracted = subtraction(newIm, newIm2)
   numIncorrect = convolution(subtracted, threshold = .9)

   cv2.namedWindow('subtracted', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('subtracted', subtracted)
   cv2.waitKey()
   #cv2.imwrite('subtracted.tif', subtracted)
   
   cv2.namedWindow('gradedKey', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('gradedKey', newIm)
   cv2.waitKey()
   #cv2.imwrite('gradedKey.tif', newIm)
     
   cv2.namedWindow('graded', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('graded', newIm2)
   cv2.waitKey()
   #cv2.imwrite('graded.tif', newIm2)

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
