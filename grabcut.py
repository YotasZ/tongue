import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('view1.jpg')
mask = np.zeros(img.shape[:2], np.uint8)#掩模
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (155, 1, 555, img.shape[0])
#(461, 820, 3)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 10, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img * mask2[:, :, np.newaxis]

cv2.imwrite('result.jpg',img)
