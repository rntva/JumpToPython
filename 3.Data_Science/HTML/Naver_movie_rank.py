import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

result = []

html = urllib.request.urlopen("http://movie.naver.com/movie/sdb/rank/rmovie.nhn")
# soupData = BeautifulSoup(html.read().decode("CP949"), "html.parser")
soupData = BeautifulSoup(html, "html.parser")
store_trs = soupData.find_all('tbody')
store_rank = soupData.find_all('img')
temp = store_rank[8:108]
tr_tag = list(store_trs[0].strings)
# k = temp[1].attrs['alt']
rank = 1
range = 1
token = 1
for x in tr_tag :
    if x != '\n' and token == 1 :
        movie_name = x
        token = 2
    elif x != '\n' and token == 2 :
        movie_chage = x
        movie_chage = temp[range].attrs['alt'] + ' ' + movie_chage
        range += 2
        token = 3
    elif token == 3 :
        result.append([rank]+[movie_name]+[movie_chage])
        token = 1
        rank += 1

nhn_movie_rank_table = DataFrame(result,columns=('movie_rank','movie_name','the range of fluctuation'))
nhn_movie_rank_table.to_csv("Naver_Movie_Rank.csv", encoding="cp949", mode='w', index=False)


# for store_tr in store_trs :
#     tr_tag = list(store_tr.strings)

# print(soup)
# print(soup.prettify())
#
# tags = soup.find_all('div', attrs={'class':'tit3'})
# print(tags)

print("End")