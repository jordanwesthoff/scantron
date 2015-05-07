import ipcv 
import numpy
import cv2

def scan_main(pdf,original):
   answers,blank = ipcv.read_in_files(pdf,original)



if __name__ == '__main__':
   import numpy
   import cv2
   pdf = 'answer_sheets.pdf'
   original = 'original.pdf'
   results = ipcv.scan_main(pdf,original)
