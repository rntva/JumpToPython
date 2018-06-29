from PIL import Image
import numpy as np
import os, re

search_dir = "D:\\Pycharm_projects\\JumpToPython\\DeepLearning\\101_ObjectCategories"
cache_dir = "D:\\Pycharm_projects\\JumpToPython\\DeepLearning\\avhash"

if os.path.exists(cache_dir) != 1 :
    os.mkdir(cache_dir)

def average_hash(fname, size = 16) :
    # fname = fname[len(search_dir) : ]

    cache_file = cache_dir + "\\" + fname[len(search_dir):-4].replace("\\", '_') + ".csv"
    try :
        img = Image.open(fname) # 이미지 데이터 열기
        img = img.convert('L') # 그레이스케일로 변환하기
        img = img.resize((size, size), Image.ANTIALIAS)

        pixel_data = img.getdata() # 픽셀 데이터 가져오기
        pixels = np.array(pixel_data) # Numpy 배열로 변환하기
        pixels = pixels.reshape((size, size)) # 2차원 배열로 변환하기
        avg = pixels.mean()
        px = 1 * (pixels > avg) # 평균보다 크면1, 작으면 0으로 변환하기
        np.savetxt(cache_file, px, fmt = "%.0f", delimiter=",")

    except :
        px = np.loadtxt(cache_file, delimiter=",")

    return px

def hammimg_dist(a, b) :
    aa = a.reshape(1, -1) # 1차원 배열로 변환
    ab = b.reshape(1, -1)
    dist = (aa != ab).sum()

    return dist

def enum_all_files(path) :
    for root, dirs, files in os.walk(path) :
        for f in files :
            fname = os.path.join(root, f)
            if re.search(r"\.(jpg|jpge|png)$",fname) :
                yield fname

def find_image(fname, rate) :
    src = average_hash(fname)
    for fname in enum_all_files(search_dir) :
        dst = average_hash(fname)
        diff_r = hammimg_dist(src, dst) / 256
        # print("[check]", fname)
        if diff_r < rate :
            yield (diff_r, fname)

# 찾기
srcfile = search_dir + "\\chair\\image_0016.jpg"
html = ""
sim = list(find_image(srcfile, 0.25))
sim = sorted(sim, key=lambda x:x[0])
for r, f in sim:
    print(r, ">", f)
    s = '<div style="float:left;"><h3>[차이:' + str(r) + '-' + \
        os.path.basename(f) + ']</h3>' + '<p><a href="' + f + '"><img src="' + \
        f + '"width=400' + '</a></p></div>'
    html += s

# HTML로 출력하기
html = """<html><head><meta charset="utf8></head>
<body><h3>원래 이미지</h3><p>
<img src='{0}' width=400></p>{1}
</body></html>""".format(srcfile,html)
with open(".avhash-search-output.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK")