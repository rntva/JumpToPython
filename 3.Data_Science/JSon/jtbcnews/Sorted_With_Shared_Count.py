import json

json_file_name = "jtbcnews_facebook_2018-01-24_2018-01-25.json"
news_share_id_name_link = []

with open(json_file_name, encoding="UTF8") as json_file_object :
    json_object = json.load(json_file_object)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)

for x in json_big_data["data"] :
    try : news_share_id_name_link.append([x["shares"]["count"]] + [x["id"]] + [x["name"]] + [x["link"]])
    except : pass

news_share_id_name_link = list(reversed(sorted(news_share_id_name_link)))

print("jtbcnews_facebook_2018-01-24_2018-01-25기사입니다.\n\
총 %d개의 기사를 공유수가 제일 많은 순서대로 제목, 링크, 공유수, ID를 출력해드립니다.\n" %len(news_share_id_name_link))
for x in news_share_id_name_link :
    print("기사제목 : %s\n링크 : %s\n공유 수 : %s\nID : %s\n"%(x[2], x[3], x[0], x[1]))
print("프로그램 종료.")