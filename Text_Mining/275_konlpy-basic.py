#py -m pip install JPype1-0.6.3-cp36-cp36m-win_amd64.whl
#py -m pip install konlpy
from konlpy.tag import Twitter

twitter = Twitter()

# malist = twitter.pos("아버지 가방에 들어가신다.", norm=True, stem=True)
malist = twitter.pos("나랏말싸미 듕귁에달아 문자와로 서르 사맛디 아니할쌔", norm=True, stem=True)

print(malist)