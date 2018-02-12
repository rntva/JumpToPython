a = """\
"title": "&quot;암호<b>화폐</b> 규제해야&quot;…노벨경제학상 스티글리츠 교수",
"originallink": "http://www.koreadaily.com/news/read.asp?art_id=5979118",
"link": "http://www.koreadaily.com/news/read.asp?art_id=5979118",
"description": "<b>가상화폐</b> 회의론자로 알려진 그가 다시 한 번 비트코인에 대해 부정적 의견을 피력한 것이다. 이어 스티글리츠 교수는 그가 이전에 언급했던 비트코인의 불법화(outlaw)가 한국이 택한 규제를 말하고, 한국으로부터 배워야... ",
"pubDate": "Thu, 25 Jan 2018 15:48:00 +0900"\
"""
a = a.replace("&quot;", '\"')
print(a)


# a = list(a)
# for x in range(len(a)) :
#     if a[x:x+6] == ['&','q','u','o','t',';'] : a[x:x+6] = ['\"']
#     elif a[x:x+3] == ['<','b','>'] : a[x:x+3] = ['']
#     elif a[x:x+4] == ['<', '/', 'b', '>', ] : a[x:x+4] = ['']
#     elif a[x:x + 4] == ['&', 'i', 't', ';', ] : a[x:x + 4] = ['<']
#     elif a[x:x + 4] == ['&', 'g', 't', ';', ] : a[x:x + 4] = ['>']
#
#
# temp = ""
# for x in a :
#     temp += str(x)
#
# print(temp)

