import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame


html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

tags =  soup.findAll('tbody')
temp_names = list(tags[0].strings)
names = []
up_downs = []
result = []
for x in temp_names :
    if x != '\n' : names.append(x)
up_down =  soup.findAll('img')
count = 1
for x in up_down[9:107] :
    try :
        kk = int(x.attrs['alt'])
    except :
        names[count] = names[count] + ' ' + x.attrs['alt']
        count += 2
for x in range(50) :
    result.append([x+1] + [names[x*2]] + [names[1+(x*2)]])

rank_table = DataFrame(result, columns=('rank','name','range'))
rank_table.to_csv("naver_rank.csv", encoding="cp949", mode= 'w', index=False)


# 과제
# 네이버 영화 랭킹 웹페이지를 분석하여 아래 형식으로 csv 파일을 생성하시오
# 순위 |      영화명       | 변동폭
#  1   |       1987        |   0
#  2   |  신과함께-죄와 벌 |  +1
#  3   |쥬만지: 새로운세계 |  -1.


print("End")