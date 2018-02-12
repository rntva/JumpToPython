import urllib.request
import datetime
import json

app_id = "uSGeu7y40ARmpLmLtouN"
app_pw = "9W8t3zFxWQ"

def replace_characters(retData) :
    retData = retData.replace("&quot;", '\\"')
    retData = retData.replace("&it;", '<')
    retData = retData.replace("&gt", '>')
    retData = retData.replace("<b>", '')
    retData = retData.replace("</b>", '')

    return retData


def get_request_url(url) :
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", app_id)
    req.add_header("X-Naver-Client-Secret", app_pw)

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e :
        print(e)
        print("[%s] Error for Url : %s" %(datetime.datetime.now(), url))

def getNaverSearchResult(sNode, search_text, page_start, display) :
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" %sNode

    parameters = "?query=%s&start=%s&display=%s"%(urllib.parse.quote(search_text), page_start, display)
    url = base + node + parameters
    retData = get_request_url(url)
    retData = replace_characters(retData)

    if retData == None : return None
    else : return json.loads(retData)

def getPostData(post, jsonResult) :
    title = post["title"]
    description = post["description"]
    org_link = post["originallink"]
    link = post["link"]

    pDate = datetime.datetime.strptime(post["pubDate"], "%a, %d %b %Y %H:%M:%S +0900")
    pDate = pDate.strftime("%Y-%m-%d %H:%M:%S")

    jsonResult.append({"title" : title, "description" : description, "org_link" : org_link, "pDate" : pDate})

def main() :
    jsonResult = []
    news_site_list = [[0, "total"]]
    # news_site_list = []
    length = 0
    news_site_list_dict = {}
    news_site_list_counting = []

    sNode = "news"
    search_next = "이명박"
    display_count = 100

    jsonSearch = getNaverSearchResult(sNode, search_next, 1, display_count)

    index = 1
    while (jsonSearch != None and jsonSearch["display"] != 0  and index < 9) :
        for post in jsonSearch["items"] :
            getPostData(post, jsonResult)

        nStart = jsonSearch["start"] + jsonSearch["display"]
        jsonSearch = getNaverSearchResult(sNode, search_next, nStart, display_count)
        index += 1
########################################################################################################
    for x in jsonResult :
        try :
            for y in range(len(news_site_list)) :
                judge = 0
                if x["org_link"].split('/')[2] == news_site_list[y][1] :
                    news_site_list[y][0] += 1
                    judge = 1
                    break
            if judge == 0 : news_site_list.append([1] + [x["org_link"].split('/')[2]])
            length += 1
        except :
            print("\t\t<에러발생 전체 출력>")
            print("title : %s\noriginal_link : %s\ndescription : %s\npubDate : %s" %(x["title"], x["org_link"], x["description"], x["pDate"]))
    news_site_list[0][0] = length
    # news_site_set = set(news_site_list)
    # for x in news_site_set :
    #     news_site_list_dict[x] = 0

    # for x in news_site_set :
    #     for y in news_site_list :
    #         if x == y :  news_site_list_dict[x] += 1
    # for x in news_site_list_dict.keys() :
    #     news_site_list_counting.append([news_site_list_dict[x]] + [x])

    news_site_list = list(reversed(sorted(news_site_list)))
    print("<건수 별 뉴스 싸이트 내림차순 정리>".center(50))
    for x in news_site_list[1:] :
        print("싸이트 : 건수 => %s : %d" %(x[1], x[0]))
    print("\t\t\t 총 건수 : %d" %news_site_list[0][0])

    # for x in jsonResult:
    #     try : news_site_list.append(x["org_link"].split('/')[2])
    #     except :
    #         print("\t\t<에러발생 전체 출력>")
    #         print("title : %s\noriginal_link : %s\ndescription : %s\npubDate : %s" %(x["title"], x["org_link"], x["description"], x["pDate"]))
    # news_site_set = set(news_site_list)
    # for x in news_site_set :
    #     news_site_list_dict[x] = 0
    #
    # for x in news_site_set :
    #     for y in news_site_list :
    #         if x == y :  news_site_list_dict[x] += 1
    # for x in news_site_list_dict.keys() :
    #     news_site_list_counting.append([news_site_list_dict[x]] + [x])
    #
    # news_site_list_counting = list(reversed(sorted(news_site_list_counting)))
    # print("<건수 별 뉴스 싸이트 내림차순 정리>".center(50))
    # for x in news_site_list_counting :
    #     print("싸이트 : 건수 => %s : %d" %(x[1], x[0]))
    # print("\t\t\t 총 건수 : %d" %len(news_site_list))

########################################################################################################
    with open("%s_naver_%s.json" %(search_next, sNode), 'w', encoding="utf8") as outfile :
        retJson = json.dumps(jsonResult, indent=4,sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print("%s_naver_%s.json SAVED" %(search_next, sNode))



if __name__ == "__main__" :
    main()