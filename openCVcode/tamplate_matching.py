import cv2 as cv  
import numpy as np 
img = cv.imread("../images/bikini.jpg")

grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face = cv.imread("../images/bikini_face.jpg",0)
left = cv.imread("../images/bikini_left.jpg",0)
right = cv.imread("../images/bikini_right.jpg",0)
left_hand = cv.imread("../images/left-hand.jpg",0)
navel =  cv.imread("../images/navle.jpg",False)
stomach =cv.imread("../images/stomach.jpg",False)

w, h =face.shape[::-1]
wl, hl = left.shape[::-1]
wr, hr = right.shape[::-1]
w_lh, h_lh = left_hand.shape[::-1]
wn, hn = navel.shape[::-1]
ws, hs = stomach.shape[::-1]
res = cv.matchTemplate(grey_img, face, cv.TM_CCOEFF_NORMED)
#print(res)
res_l = cv.matchTemplate(grey_img, left, cv.TM_CCOEFF_NORMED)
#print(res_l)
res_r = cv.matchTemplate(grey_img, right,cv.TM_CCORR_NORMED)
#print(res_r)
res_lh =cv.matchTemplate(grey_img, left_hand, cv.TM_CCORR_NORMED)
res_n  = cv.matchTemplate(grey_img ,navel, cv.TM_CCORR_NORMED)
res_s = cv.matchTemplate(grey_img, stomach, cv.TM_CCORR_NORMED)
threshold = 0.666;
threshold_l = 0.822;
threshold_r = 0.8912;
threshold_lh = 0.9878
threshold_n = .99844
threshold_s = .991254
loc = np.where(res >= threshold)
#print(loc)
loc_l = np.where(res_l>= threshold_l)
#print(loc_l)
loc_r = np.where(res_r>=threshold_r)
#print(loc_r)
loc_lh = np.where(res_lh>=threshold_lh)
#print(loc_lh)
loc_n = np.where(res_n>= threshold_n)
#print(loc_n)
loc_s = np.where(res_s>=threshold_s)
#print(loc_s)
for pt in zip(*loc[::-1]):
    cv.putText(img, "BM face",(pt[0]+w-130, pt[1]+h-157), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,0,255))
    cv.rectangle(img,pt, (pt[0]+w, pt[1]+h), (0,255,0),2)
    
for i in zip(*loc_l[::-1]):
    cv.putText(img, "Left boobs",(i[0]+wl-140, i[1]+hl-175), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,0,255))
    cv.rectangle(img,i, (i[0]+wl, i[1]+hl),(0,255,0),2)

for r in zip(*loc_r[::-1]):

    cv.putText(img, "Right boobs",(r[0]+wr-154, r[1]+hr-175), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,0,255))
    cv.rectangle(img, r, (r[0]+wr, r[1]+hr),(0,255,0),2)
for lh in zip(*loc_lh[::-1]):

    cv.putText(img, "Left hand",(lh[0]+w_lh-150, lh[1]+h_lh-107), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,0,255))
    cv.rectangle(img, lh, (lh[0]+w_lh, lh[1]+h_lh),(0,255,0),2)
for n in zip(*loc_n[::-1]):
    
    cv.putText(img, "Navel",(n[0]
    +wn-54, n[1]+hn-80), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,0,255))
    cv.rectangle(img, n, (n[0]+wn, n[1]+hn),(0,255,0),2)
for s in zip(*loc_s[::-1]):
    
    cv.putText(img, "Belly",(s[0]+ws-286, s[1]+hs-210), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,0,255))
    cv.rectangle(img, s, (s[0]+ws, s[1]+hs),(0,255,0),2)



cv.imshow("Bikini Model  ", img)
cv.waitKey(False)
cv.destroyAllWindows()
