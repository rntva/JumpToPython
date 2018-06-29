import cv2, sys, re
import os

image_file = "image2.jpg"

# 출력 파일 이름
output_file = re.sub(r'\,jpg|jpeg|PNG$','-mosaic.jpg', image_file)
mosaic_rate = 15

# 캐스캐이드 파일 경로 지정하기
cascade_file = 'cascades/data/haarcascade_frontalface_alt.xml'

# 이미지 읽어 들이기
image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환

# 얼굴 인식 실행하기
cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=3, minSize=(40, 40))

if len(face_list) == 0:
    print("no face")
    quit()

# 확인한 부분에 모자이크 걸기
print(face_list)
color = (0, 0, 255)

for (x, y, w, h) in face_list:
    # 얼굴 부분 자르기
    face_img = image[y:y+h, x:x+w]
    # 자른 이미지를 지정한 배율로 확대/축소하기
    face_img = cv2.resize(face_img, (w//mosaic_rate, h//mosaic_rate))
    # 확대/축소한 그림을 원래 크기로 돌리기
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)

    # 원래 이미지에 붙이기
    image[y:y+h, x:x+w] = face_img

# 렌더링 결과를 파일에 출력
if not os.path.exists("res_Img"):
    os.mkdir("res_Img")
cv2.imwrite("res_Img/mosaic-output2.PNG", image)