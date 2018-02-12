import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

basic_url = "https://www.youtube.com/results?sp=CAASAhAB&search_query="
search_query = urllib.parse.quote_plus(input("찾으시는 영상의 검색어를 입력해 주십시오. : "))
final_url = basic_url+search_query
try :
    response = urllib.request.urlopen(final_url)
except Exception as e :
    print(e)
retData = response.read().decode("utf-8")
soup_test = BeautifulSoup(retData, 'html.parser')
temp_list = soup_test.findAll("div", attrs={"class":"yt-lockup-content"})
index = 0
for index in range(len(temp_list)-1) :
    try:
        print(temp_list[index+1].contents[0].text) #동영상 제목 - 길이
        print("https://www.youtube.com" + temp_list[index+1].contents[0].contents[0].attrs["href"]) #/watch?v=e_Qt-jCMG10 주소?를 얻을 수 있다.
        print(temp_list[index+1].contents[1].text) #게시자
        print(temp_list[index + 1].contents[2].contents[0].contents[1].text)  # 조회수
    except Exception as e : print(e)
    print()

print("%d개" %(len(temp_list)-1))
print("프로그램 종료.")
