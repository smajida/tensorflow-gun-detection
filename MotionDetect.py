import cv2                            # importing Python OpenCV
from datetime import datetime
import os

os.chdir('/home/nvidia/Desktop/Motion-Images')# importing datetime for naming files w/ timestamp

def diffImg(t0, t1, t2):              # Function to calculate difference between images.
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

threshold = 150000                     # Threshold for triggering "motion detection"
cap = cv2.VideoCapture(1)             # Lets initialize capture on webcam

winName = "Movement Indicator"		    # comment to hide window
cv2.namedWindow(winName)		          # comment to hide window

# Read three images first:
t_minus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
# Lets use a time check so we only take 1 pic per sec
timeCheck = datetime.now().strftime('%Ss')

while True:
  cv2.imshow( winName, cap.read()[1] )
  print(cv2.countNonZero(diffImg(t_minus, t, t_plus)))		# comment to hide window
  if cv2.countNonZero(diffImg(t_minus, t, t_plus)) > threshold and timeCheck != datetime.now().strftime('%Ss'):
    dimg= cap.read()[1]
    cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg', dimg)
  timeCheck = datetime.now().strftime('%Ss')
  # Read next image
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)

  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)			# comment to hide window
    break
