import urllib.request
import datetime
import json

app_id = "uSGeu7y40ARmpLmLtouN"
app_pw = "9W8t3zFxWQ"

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

    if retData == None : return None
    else : return json.loads(retData)

def getPostData(post, jsonResult) :
    title = post["title"]
    description = post["description"]
    org_link = post["originallink"]
    link = post["link"]

    pDate = datetime.datetime.strptime(post["pubDate"], "%a, %d %b %Y %H:%M:%S + 0900")
    pDate = pDate.strftime("%Y-%m-%d %H:%M:%S")

    jsonResult.append({"title" : title, "description" : description, "org_link" : org_link, "pDate" : pDate})

def main() :
    jsonResult = []

    sNode = "news"
    search_next = "가상화폐"
    display_count = 100

    jsonSearch = getNaverSearchResult(sNode, search_next, 1, display_count)

    index = 1
    while (jsonSearch != None and jsonSearch["display"] != 0  and index < 9) :
        for post in jsonSearch["items"] :
            getPostData(post, jsonResult)
        nStart = jsonSearch["start"] + jsonSearch["display"]
        jsonSearch = getNaverSearchResult(sNode, search_next, nStart, display_count)
        index += 1

    with open("%s_naver_%s.json" %(search_next, sNode), 'w', encoding="utf8") as outfile :
        retJson = json.dumps(jsonResult, indent=4,sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print("%s_naver_%s.json SAVED" %(search_next, sNode))

if __name__ == "__main__" :
    main()