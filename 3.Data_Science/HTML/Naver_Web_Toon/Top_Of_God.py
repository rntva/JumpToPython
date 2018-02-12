import urllib.request

for x in range(1, 74) :
    img_url = "http://imgcomic.naver.net/webtoon/183559/366/20171222150810_363d163ed237ac4b002005275285e1cf_IMAG01_%s.jpg" %x
    saving_dir_name = "Top_Of_God\\pairate_x.jpg"
    urllib.request.urlretrieve(img_url, saving_dir_name)
    print("나쁜짓은 재미있어")
