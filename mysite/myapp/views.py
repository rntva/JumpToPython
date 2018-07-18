import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
bookmarks = [{'site': 'Naver', 'url': "https://www.naver.com"},
             {'site': 'Daum', 'url': "https://www.daum.net"},
             {'site': 'Google', 'url': "https://www.google.co.kr"}]

def home(request) :
    title = request.GET.get("title")
    aaa = request.GET.get("aaa")
    contents = {"title" : title,
                "aaa" : aaa}
    return render(request, "home.html", contents)

def member_list(request) :
    members = [{'name': 'Hong', 'age': 20},
               {'name': 'Kim', 'age': 22},
               {'name': 'Song', 'age': 30}]
    context = {'members': members}

    for member in members :
        print("member : ", member)

    return render(request, 'memberList.html', context)

def bookmark_list(request) :
    global bookmarks
    site = request.GET.get("site")
    url = request.GET.get("url")

    if site :
        bookmark = {"site" : site, "url" : url}
        bookmarks.append(bookmark)

    context = {'BML': bookmarks}

    for bookmark in bookmarks :
        print("bookmark : ", bookmark)

    return render(request, 'bookMarksList.html', context)

def set_led(request) :
    led = request.GET.get("led")
    context = {"led" : led}
    return render(request, 'led.html', context)

# def bookmark_list(request) :
#     global bookmarks
#     site = request.GET.get("site")
#     url = request.GET.get("url")
#
#     if site :
#         bookmark = {"site" : site, "url" : url}
#         bookmarks.append(bookmark)
#
#     context = {'BML': bookmarks}
#
#     for bookmark in bookmarks :
#         print("bookmark : ", bookmark)
#
#     return HttpResponse(json.dumps(context), content_type='application/json')
