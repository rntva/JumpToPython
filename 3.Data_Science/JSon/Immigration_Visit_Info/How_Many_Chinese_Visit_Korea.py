import urllib.request
import datetime
import json
import math

access_key = "R9tidMCdl2pvpCuE0n4%2Fh%2FcPJIqFtgn3Vvp6UmSAWEpTQ4GbAwJ8n4O7IGhux4Vcm49bSCh64Md81lSPvY4dTQ%3D%3D"


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
def getTourPointVisitor(yyyymm, nat_cd, nPagenum, nItems) :
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getForeignTuristStatsList"
    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + str(nat_cd)
    parameters += "&SEX_CD="
    parameters += "&AGE_CD="
    parameters += "&TRA_PURP_CD="
    parameters += "&PORT_CD="
    parameters += "&pageNo=" + str(nPagenum)
    parameters += "&numOfRows=" + str(nItems)
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
    nation_num = 112 #중국
    port = "중국인"
    # natKorNm = ''
    nPagenum = 1
    nTotal = 0
    nItems = 100
    nStartYear = 2011
    nEndYear = 2012
    debug_index = 0

    for year in range(nStartYear, nEndYear) :
        for month in range(1,13) :
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            nPagenum = 1

            #[CODE 3]
            while 1 :
                jsonData = getTourPointVisitor(yyyymm, nation_num, nPagenum, nItems)

                if jsonData["response"]["header"]["resultMsg"] == "OK" :
                    nTotal = jsonData["response"]["body"]["totalCount"]
                    if nTotal == 0 : break
                    if debug_index == 1687:
                        print("Break Point")
                    for item in jsonData["response"]["body"]["items"]["item"] :
                        getTourPointData(yyyymm, item, jsonResult)
                        debug_index +=1
                        print("debug index", debug_index)

                    nPage = math.ceil(nTotal/100)
                    if nPagenum == nPage : break
                    nPagenum += 1

                else : break

    with open("%s_입국정보_%d_%d.json" %(port, nStartYear, nEndYear-1), 'w', encoding="utf-8") as outfile :
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print("%s_입국정보_%d_%d.json SAVED" %(port, nStartYear, nEndYear-1))

if __name__ == "__main__" :
    main()