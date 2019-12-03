import cv2 as cv  
import numpy as np 
img = cv.imread("../images/disney.jpg")

grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face = cv.imread("../images/disney_face.jpg",0)
left = cv.imread("../images/disney_top.jpg",0)
right = cv.imread("../images/disney_btw.jpg",0)
left_hand = cv.imread("../images/disney_target.jpg",0)


w, h =face.shape[::-1]
wl, hl = left.shape[::-1]
wr, hr = right.shape[::-1]
w_lh, h_lh = left_hand.shape[::-1]

res = cv.matchTemplate(grey_img, face, cv.TM_CCOEFF_NORMED)
#print(res)
res_l = cv.matchTemplate(grey_img, left, cv.TM_CCOEFF_NORMED)
#print(res_l)
res_r = cv.matchTemplate(grey_img, right,cv.TM_CCORR_NORMED)
#print(res_r)
res_lh =cv.matchTemplate(grey_img, left_hand, cv.TM_CCORR_NORMED)

threshold = 0.7
threshold_l = 0.77;
threshold_r = 0.96
threshold_lh = 0.9814

loc = np.where(res >= threshold)
print("loc: ", loc)
loc_l = np.where(res_l>= threshold_l)
print("loc_l: ", loc_l)
loc_r = np.where(res_r>=threshold_r)
print("loc_r ", loc_r)
loc_lh = np.where(res_lh>=threshold_lh)
print("loc_lh: ",loc_lh)

for pt in zip(*loc[::-1]):
    cv.putText(img, "face",(pt[0]+w-57, pt[1]+h-75), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0,0,255))
    cv.rectangle(img,pt, (pt[0]+w, pt[1]+h), (0,255,0),1)
    
for i in zip(*loc_l[::-1]):
    cv.putText(img, "upperbody",(i[0]+wl-178, i[1]+hl-184), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0,0,255))
    cv.rectangle(img,i, (i[0]+wl, i[1]+hl),(0,255,0),1)

for r in zip(*loc_r[::-1]):

    cv.putText(img, "chest",(r[0]+wr-74, r[1]+hr-71), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0,0,255))
    cv.rectangle(img, r, (r[0]+wr, r[1]+hr),(0,255,0),1)
for lh in zip(*loc_lh[::-1]):

    cv.putText(img, "target",(lh[0]+w_lh-30, lh[1]+h_lh-38), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (0,0,255))
    cv.rectangle(img, lh, (lh[0]+w_lh, lh[1]+h_lh),(0,255,0),1)


cv.imshow("Disney", img)
cv.waitKey(False)
cv.destroyAllWindows()
