import numpy as np
import cv2
from matplotlib import pyplot as plt
import ipcv
import cv

def testRotation2():
   print 'hello'
   #sheets, img2 = ipcv.read_in_files('answer_sheets.pdf','original_scan_sheet.pdf')
   #colorimg1 = cv2.imread('test0001.tif', 0)          # queryImage
   #colorimg2 = cv2.imread('original.tif', 0)
   #print colorimg1
   colorimg1 = cv2.imread('girlRotated.jpeg')
   colorimg2 = cv2.imread('girl.jpeg')

   numRows, numCols, numBands, dataType = ipcv.dimensions(colorimg1)
   if numBands == 3:
      image1 = cv2.cvtColor(colorimg1, cv.CV_BGR2GRAY)
   elif numBands == 1:
      image1 = colorimg1

   numRows2, numCols2, numBands2, dataType2 = ipcv.dimensions(colorimg2)
   if numBands2 == 3:
      image2 = cv2.cvtColor(colorimg2, cv.CV_BGR2GRAY)
   elif numBands2 == 1:
      image2 = colorimg2
   #image1 = cv2.GaussianBlur(image1,(5,5),0)
   #image2 = cv2.GaussianBlur(image2,(5,5),0)
   mask = np.zeros((numRows, numCols)).astype(np.uint8)
   #3 circles
   #mask[690:773,19:105] = 1
   #mask[15:100,512:603] = 1
   #mask[700:780,490:590] = 1
   #First Name
   mask[25:43,230:347] = 1
   #3 Half Circles
   #mask[715:761,62:82] = 1
   #mask[712:776,548:568] = 1
   #mask[27:80,561:581] = 1
   #mask[375:385,146:206] = 1
   #Quarter Circle
   #mask[59:80,561:581] = 1
   #Additional Information
   mask[190:203,367:480] = 1
   #University ID
   mask[24:38,364:484] = 1
   #Last
   mask[25:35,70:92] = 1

   cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
   cv2.imshow('mask', mask)
   cv2.waitKey()
   print 'mask dataType', mask.dtype
   print 'img1 datatype', image1.dtype
   print 'img2 datatype', image2.dtype
   #img2 = cv2.imread('scene.jpeg',0) # trainImage

   #initiate SIFT detector
   sift = cv2.SIFT()

   # find the keypoints and descriptors with SIFT
   keypoint1, descriptor1 = sift.detectAndCompute(image1,None)
   keypoint2, descriptor2 = sift.detectAndCompute(image2,None)
   print 'keypoint1', keypoint1
   # A combo of FAST and BRIEF
   #orb = cv2.ORB()
   #keypoint1, descriptor1 = orb.detectAndCompute(image1,None)
   #keypoint2, descriptor2 = orb.detectAndCompute(image2,None)

   i_params = dict(algorithm=0, trees=5)
   s_params = dict(checks=50)

   flann = cv2.FlannBasedMatcher(i_params, s_params)
   matches = flann.knnMatch(descriptor1, descriptor2, k=2)

   good_matches = []

   for m, n in matches:
      if m.distance < 0.7*n.distance:
         good_matches.append(m)

   src_points = np.float32([keypoint1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
   dst_points = np.float32([keypoint2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

   print 'test', src_points
   print 'original', dst_points

   # create BFMatcher object
   #bfObject = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

   # Match descriptors.
   #matches = bfObject.match(descriptor1,descriptor2)

   # Sort them in the order of their distance.
   good_matches = sorted(good_matches, key = lambda x:x.distance)

   # Draw first 10 matches.
   image3 = drawMatches(image1,keypoint1,image2,keypoint2,good_matches[:10])  
   #image3 = drawMatches(image1,src_points.astype(np.uint8),image2, dst_points(np.uint8),good_matches[:10])
   cv2.imwrite('matching.tif', image3)

   #Create Affine Transform
   M = cv2.getAffineTransform(src_points[0:3], dst_points[0:3])
   print M
   dst = cv2.warpAffine(image1, M, (numRows, numCols))
   print np.min(dst), np.max(dst)
   cv2.namedWindow('rotatedIm', cv2.WINDOW_AUTOSIZE)
   cv2.imshow('rotatedIm', dst.astype(np.uint8))
   cv2.waitKey()
def drawMatches(img1, kp1, img2, kp2, matches):
    """
    My own implementation of cv2.drawMatches as OpenCV 2.4.9
    does not have this function available but it's supported in
    OpenCV 3.0.0

    This function takes in two images with their associated 
    keypoints, as well as a list of DMatch data structure (matches) 
    that contains which keypoints matched in which images.

    An image will be produced where a montage is shown with
    the first image followed by the second image beside it.

    Keypoints are delineated with circles, while lines are connected
    between matching keypoints.

    img1,img2 - Grayscale images
    kp1,kp2 - Detected list of keypoints through any of the OpenCV keypoint 
              detection algorithms
    matches - A list of matches of corresponding keypoints through any
              OpenCV keypoint matching algorithm
    """

    # Create a new output image that concatenates the two images together
    # (a.k.a) a montage
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]

    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')

    # Place the first image to the left
    out[:rows1,:cols1,:] = np.dstack([img1, img1, img1])
     # Place the next image to the right of it
    out[:rows2,cols1:cols1+cols2,:] = np.dstack([img2, img2, img2])

    # For each pair of points we have between both images
    # draw circles, then connect a line between them
    for mat in matches:

        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        # x - columns
        # y - rows
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt

        # Draw a small circle at both co-ordinates
        # radius 4
        # colour blue
        # thickness = 1
        cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)   
        cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)

        # Draw a line in between the two points
        # thickness = 1
        # colour blue
        cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)

    # Show the image
    cv2.imshow('Matched Features', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return out

if __name__ == "__main__":
   testRotation2()
