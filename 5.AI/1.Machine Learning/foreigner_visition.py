import urllib.request
import datetime
import json
import math
import sys
import os
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

access_key = "DthpXT7YzG6wllvd7zn6DyNRVJJGmVR2EGEs5UWg%2BeVXHyMkw%2FxNO2WcSwTZc9RX0sJzCK5d3bNOxD16Etj0%2Fg%3D%3D"


def get_request_url(url) :
    req = urllib.request.Request(url)

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e :
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None

#[CODE1]
def getNatVisitor(yyyymm, nat_cd, ed_cd) :
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + str(nat_cd)
    parameters += "&ED_CD=" + ed_cd
    url = end_point + parameters

    retData = get_request_url(url)
    if retData == None : return None
    else : return json.loads(retData)

#[CODE2]
def getTourPointData(yyyymm, item, jsonResult) :
    try :
        age = '' if "age" not in item.keys() else item["age"]
        natKorNm = '' if "natKorNm" not in item.keys() else item["natKorNm"]
        port = '' if "port" not in item.keys() else item["port"]
        sex = '' if "sex" not in item.keys() else item["sex"]
        traPurp = 0 if "traPurp" not in item.keys() else item["traPurp"]

        jsonResult.append({"yyyymm" : yyyymm, "age" : age, "natKorNm" : natKorNm, "port" : port, "sex" : sex, "traPurp" : traPurp})
    except Exception as e :
        print("이게 문제다 : ", end='')
        print(e)

def main() :
    jsonResult = []
    nation_num = "112" #중국
    ed_cd = "E"

    nStartYear = 2011
    nEndYear = 2012


    for year in range(nStartYear, nEndYear) :
        for month in range(1,13) :
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            jsonData = getNatVisitor(yyyymm, nation_num, ed_cd)

            if jsonData["response"]["header"]["resultMsg"] == "OK" :
                krName = jsonData["response"]["body"]["items"]["item"]["natKorNm"]
                krName = krName.replace(' ','')
                iTotalVisitor = jsonData["response"]["body"]["items"]["item"]["num"]
                print("%s_%s : %s" %(krName, yyyymm, iTotalVisitor))

                jsonResult.append({"nat_name" : krName, "nat_cd" : nation_num, "yyyymm" : yyyymm, "visit_cnt" : iTotalVisitor})

    cnVisit = []
    VisitYM = []
    index = []

    i = 0

    for item in jsonResult :
        index.append(i)
        cnVisit.append(item["visit_cnt"])
        VisitYM.append(item["yyyymm"])
        i += 1

    with open("%s(%s)_입국정보_%d_%d.json" %(krName, nation_num, nStartYear, nEndYear-1), 'w', encoding="utf-8") as outfile :
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print("%s(%s)_입국정보_%d_%d.json SAVED" %(krName, nation_num, nStartYear, nEndYear-1))

    font_location = "c:/windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc("font", family=font_name)

    plt.xticks(index, VisitYM)
    plt.plot(index, cnVisit)
    plt.xlabel("방문원")
    plt.ylabel("방문객수")
    plt.grid(True)
    plt.show()

if __name__ == "__main__" :
    main()