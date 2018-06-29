# import sys
# import numpy as np
# import cv2
# import ocr_minst
#
# # MNIST 학습 데이터 일어 들이기
# mnist = ocr_minst.build_model()
# mnist.load_weights("mnist.hdf5")
#
# # 이미지 읽어 들이기
# im = cv2.imread("1to100.jpg")
#
# # 그레이스케일로 변환하고 블러를 걸고 이진화하기
# gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (5, 5), 0)
# thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
# cv2.imwrite("1to100-th.png", thresh)
#
# # 윤곽 추출하기
# contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
# # contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1] # 숫자 인식 정확도를 위해
#
# # 추출한 좌표 정리하기
# rects = []
# im_w = im.shape[1]
# for i, cnt in enumerate(contours) :
#     x, y, w, h = cv2.boundingRect(cnt)
#     if w < 10 or h < 10 : continue
#     if w > im_w / 5 : continue # 너무 작으면 건너뛰기
#     y2 = round(y / 10) * 10
#     index = y2 * im_w + x
#     rects.append((index, x, y, w, h))
# rects = sorted(rects, key=lambda x : x[0]) # 정렬하기
#
# # 해당 영역의 이미지 데이터 추출하기
# X = []
# for i, r in enumerate(rects) :
#     index, x, y, w, h, = r
#     num = gray[y : y + h, x : x + w] # 부분 이미지 추출하기
#     num = 255 - num # 반전하기
#
#     # 정사각형 내부에 그림 옮기기
#     ww = round((w if w > h else h) * 1.85)
#     spc = np.zeros((ww, ww))
#     wy = (ww - h) // 2
#     wx = (ww - w) // 2
#     spc[wy : wy + h, wx : wx + w] = num
#     num = cv2.resize(spc, (28, 28)) # MNIST 크기 맞추기
#     # cv2.imwrite(str(i) + "-num.png", num) # 자른 문자 저장하기
#
#     #데이터 정규화
#     num = num.reshape(28 * 28)
#     num = num.astype("float32") / 255
#     X.append(num)
#
# # s = """1 2 3 4 5 6 7 8 9 10\
# # 11 12 13 14 15 16 17 18 19 20\
# # 21 22 23 24 25 26 27 28 29 30\
# # 31 32 33 34 35 36 37 38 39 40\
# # 41 42 43 44 45 46 47 48 49 50\
# # 51 52 53 54 55 56 57 58 59 60\
# # 61 62 63 64 65 66 67 68 69 70\
# # 71 72 73 74 75 76 77 78 79 80\
# # 81 82 83 84 85 86 87 88 89 90\
# # 91 92 93 94 95 96 97 98 99 100"""
#
# s = "12345678910" + \
#     "11121314151617181920" + \
#     "21222324252627282930" + \
#     "31323334353637383940" + \
#     "41424344454647484950" + \
#     "51525354555657585960" + \
#     "61626364656667686970" + \
#     "71727374757677787980" + \
#     "81828384858687888990" + \
#     "919293949596979899100"
#
# answer = list(s)
# ok = 0
# nlist = mnist.predict(np.array(X))
# for i, n in enumerate(nlist) :
#     ans = n.argmax()
#     if ans == int(answer[i]) :
#         ok += 1
#     else :
#         print("[ng]", i, "번째", ans, "!=", answer[i], np.int32(n * 100))
# print("정답률 : ", ok / len(nlist))
#
# # cv2.imwrite("numbers-cnt3.png", im)

import sys
import numpy as np
import cv2
# import ocr_minst
import ocr_MnistFinal

# MNIST 학습 데이터 읽어 들이기
# mnist = ocr_minst.build_model()
# mnist.load_weights('mnist.hdf5')
mnist = ocr_MnistFinal.build_model()
mnist.load_weights('font_draw.hdf5')
# 이미지 읽어 들이기
# 이미지 읽어 들이기
# im = cv2.imread('1to100.jpg')
im = cv2.imread('pie.png')
# 윤곽 추출하기
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # 그레이스케일로 변환하기
blur = cv2.GaussianBlur(gray, (5, 5), 0) # 블러
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2) # 2진화
# cv2.imwrite("numbers100-th.PNG", thresh)
cv2.imwrite("pie-th.PNG", thresh)
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]

# 추출한 좌표 정렬하기
rects = []
im_w = im.shape[1]
for i, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    if w < 10 or h < 10: continue # 너무 작으면 생략하기
    if w > im_w / 5: continue # 너무 크면 생략하기
    y2 = round(y/10) * 10 # Y 좌표 맞추기
    index = y2 * im_w + x
    rects.append((index, x, y, w, h))
rects = sorted(rects, key=lambda x:x[0]) # 정렬하기

# 해당 영역의 이미지 데이터 추출하기
X = []
for i, r in enumerate(rects):
    index, x,y,w,h = r
    num = gray[y:y+h, x:x +w] # 부분 이미지 추출하기
    num = 255 - num # 반전하기
    # 정사각형 내부에 그림 옮기기
    ww = round((w if w > h else h) * 1.85)
    spc = np.zeros((ww, ww))
    wy = (ww-h)//2
    wx = (ww-w)//2
    spc[wy:wy+h, wx:wx+w] = num
    num = cv2.resize(spc, (28, 28)) # MNIST 크기 맞추기
    # cv2.imwrite(str(i)+"-num.PNG", num) # 자른 문자 저장하기
    # 데이터 정규화
    num = num.reshape(28*28)
    num = num.astype("float32") / 255
    X.append(num)

# 예측하기

# s = "12345678910" + \
#     "11121314151617181920" + \
#     "21222324252627282930" + \
#     "31323334353637383940" + \
#     "41424344454647484950" + \
#     "51525354555657585960" + \
#     "61626364656667686970" + \
#     "71727374757677787980" + \
#     "81828384858687888990" + \
#     "919293949596979899100"

s = "31415926535897932384" + \
    "62643383279502884197" + \
    "16939937510582097494" + \
    "45923078164062862089" + \
    "98628034825342117067"

answer = list(s)
ok = 0
nlist = mnist.predict(np.array(X))
for i, n in enumerate(nlist):
    ans = n.argmax()
    if ans == int(answer[i]):
        ok += 1
    else:
        print("[ng]", i, "번째", ans, "!=", answer[i], np.int32(n*100))
print("정답률:", ok/len(nlist))
