import urllib.request
import datetime
import json
import threading
import time

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_Dehumidifier = False
g_Humidifier = False
g_AI_Mode = False

accesskey = "R9tidMCdl2pvpCuE0n4%2Fh%2FcPJIqFtgn3Vvp6UmSAWEpTQ4GbAwJ8n4O7IGhux4Vcm49bSCh64Md81lSPvY4dTQ%3D%3D"

def get_request_url(url) :
    req = urllib.request.Request(url) #Request를 쓰면 프로토콜 레벨에서 채워질 값이 들어간다.

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print("[%s] Url Request Successed" %datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e :
        print(print("[%s] Url Request Failed" % datetime.datetime.now()))
        print(e)
        return None

def get_weather_history_info(x_coordinate, y_coordinate, base_date, base_time, page_num) :
    basic_request_url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json"
    parameters += "&ServiceKey=" + accesskey
    parameters += "&nx=" + x_coordinate
    parameters += "&ny=" + y_coordinate
    parameters += "&base_date=" + base_date
    parameters += "&base_time=" + base_time
    parameters += "&pageNo=" + str(page_num)

    final_request_url = basic_request_url + parameters
    retData = get_request_url(final_request_url)

    if retData == None : return None
    else : return json.loads(retData)

def process_weather_info() :
    now_page = 1
    now_date = datetime.datetime.now()
    base_date = str(now_date.year) + "{0:0>2}".format(str(now_date.month)) + "{0:0>2}".format(str(now_date.day))
    if now_date.minute >= 45 :
        base_time = "{0:0>2}".format(str(now_date.hour)) + "{0:0>2}".format(str(now_date.minute))
    else :
        base_time = "{0:0>2}".format(str(now_date.hour - 1)) + "{0:0>2}".format(str(now_date.minute))

    while 1 :
        jsonData = get_weather_history_info("89", "91", base_date, base_time, now_page)
        if jsonData["response"]["header"]["resultMsg"] == "OK" :
            for item in jsonData["response"]["body"]["items"]["item"] :
                name_of_coordinate = "대구광역시 동구 신암4동"
                jsonResult.append({"name" : name_of_coordinate,
                                   "base_date" : item["baseDate"],
                                   "base_time" : item["baseTime"],
                                   "weather" : item["category"],
                                   "forecast_data" : item["fcstDate"],
                                   "forecast_time" : item["fcstTime"],
                                   "weather_value" : item["fcstValue"]})
        now_page += 1
        max_pageNo = int(jsonData["response"]["body"]["totalCount"] / jsonData["response"]["body"]["numOfRows"])
        if max_pageNo - now_page == -1 : break
    return None

def save_weather_info(data, name = "우리동내_초단기_예보조회.json") :
    with open(name, 'w', encoding="utf-8") as outfile :
        retJson = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    return  None

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 시뮬레이션 모드")
    print("5. 프로그램 종료")


def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True :
        if device_name == "난방기" or device_name == "가습기" or device_name == "제습기" :
            print("작동") #HK Comment]  장비에 맞는 상태 메세지 변경
        elif device_name == "발코니(베란다) 창문" or device_name == "출입문" or device_name == "가스밸브" :
            print("열림")
    else :
        if device_name == "난방기" or device_name == "가스벨브" or device_name == "가습기" or device_name == "제습기" :
            print("정지") #HK Comment]  장비에 맞는 상태 메세지 변경
        elif device_name == "발코니(베란다) 창문" or device_name == "출입문" or device_name == "가스밸브" :
            print("닫힘")

def check_device_status():
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문', g_Door)
    print_device_status("가습기", g_Humidifier)
    print_device_status("제습기", g_Dehumidifier)


def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")
    print("5. 가습기")
    print("6. 제습기")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_Humidifier, g_Dehumidifier

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door
    if menu_num == 5: g_Humidifier = not g_Humidifier
    if menu_num == 6: g_Dehumidifier = not g_Dehumidifier

    check_device_status()

def get_realtime_weather_info_countinusly() :
    temp = datetime.datetime.now()
    if temp.minute >= 45 and temp.minute < 46 :
        if g_AI_Mode == True : process_weather_info()
        else : pass
        time.sleep(60)
    elif temp.minute < 45 :
        sleep_time_2 = (45 - temp.minute) * 60 - temp.second
        time.sleep(sleep_time_2)
    elif temp.minute >= 46 :
        sleep_time_1 = (60 - temp.minute) * 60 - temp.second
        time.sleep(sleep_time_1)

def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else:print("중지")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동\n우리동내 초단기예보 자동갱신 시작")
            # t = threading.Thread(target=get_realtime_weather_info_countinusly())
            # t.daemon = True
            # t.start()

        else: print("중지")
    elif menu_num == 3:
        process_weather_info()
        save_weather_info(jsonResult)
        if g_AI_Mode == True :
            radiator_control(jsonResult)
            # window_control(jsonResult)
            humidifier_control(jsonResult)
            dehumidifier_control(jsonResult)

def radiator_control(json_data) :
    global g_Radiator
    for item in json_data:
        if item["weather"] == "T1H" and item["weather_value"] >= 20 and g_Radiator == True:
            print("20도 이상이 예상되어 난방기를 끕니다.")
            g_Radiator = not g_Radiator
            break
        elif item["weather"] == "T1H" and item["weather_value"] < 20 and g_Radiator == False:
            print("20도 미만이 예상되어 난방기를 켭니다.")
            g_Radiator = not g_Radiator
            break

def window_control(json_data) :
    global g_Balcony_Windows
    for item in json_data:
        if item["weather"] == "PTY" and item["weather_value"] != 0 and g_Balcony_Windows == True:
            print("비/눈이 내리는 것이 예상되어 창문을 닫습니다.")
            g_Balcony_Windows = not g_Balcony_Windows
            break
        elif item["weather"] == "PTY" and item["weather_value"] == 0 and g_Balcony_Windows == False:
            print("날이 좋을 것으로 예상되어 창문이 닫혀 있으니 엽니다.")
            g_Balcony_Windows = not g_Balcony_Windows
            break

def dehumidifier_control(json_data) :
    global g_Dehumidifier
    for item in json_data :
        if item["weather"] == "REH" and item["weather_value"] > 70 and g_Dehumidifier == False:
            print("습도가 70%초과라 예상되어 제습기를 켭니다.")
            g_Dehumidifier = not g_Dehumidifier
            # if g_Humidifier == True : g_Humidifier = not g_Humidifier
            break
        elif item["weather"] == "REH" and item["weather_value"] <= 70 and g_Dehumidifier == True:
            print("습도가 70%이하라 예상되어 제습기를 끕니다.")
            g_Dehumidifier = not g_Dehumidifier
            break

def humidifier_control(json_data) :
    global g_Humidifier
    for item in json_data :
        if item["weather"] == "REH" and item["weather_value"] < 40 and g_Humidifier == False:
            print("습도가 40%미만이라 예상되어 가습기를 켭니다.")
            g_Humidifier = not g_Humidifier
            # if g_Dehumidifier == True : g_Dehumidifier = not g_Dehumidifier
            break
        elif item["weather"] == "REH" and item["weather_value"] >= 40 and g_Humidifier == True:
            print("습도가 40%이상이라 예상되어 가습기를 끕니다.")
            g_Humidifier = not g_Humidifier
            break

def simulation_mode() :
    # with open("우리동내_초단기_예보조회.json", encoding="utf-8") as json_file_object :
    #     json_object = json.load(json_file_object)
    #     json_string = json.dumps(json_object)
    #     json_big_data = json.loads(json_string)
    global g_Balcony_Windows
    global g_Humidifier
    global g_Dehumidifier

    json_simulation_data = [
        {
            "base_date": 20180130,
            "base_time": "0930",
            "forecast_data": 20180130,
            "forecast_time": 1000,
            "name": "대구광역시 동구 신암4동",
            "weather": "PTY",
            "weather_value": 1
        },
        {
            "base_date": 20180130,
            "base_time": "0930",
            "forecast_data": 20180130,
            "forecast_time": 1000,
            "name": "대구광역시 동구 신암4동",
            "weather": "REH",
            "weather_value": 80
        }
    ]

    json_simulation_data_good_weather = [
        {
            "base_date": 20180130,
            "base_time": "0930",
            "forecast_data": 20180130,
            "forecast_time": 1000,
            "name": "대구광역시 동구 신암4동",
            "weather": "PTY",
            "weather_value": 0
        },
        {
            "base_date": 20180130,
            "base_time": "0930",
            "forecast_data": 20180130,
            "forecast_time": 1000,
            "name": "대구광역시 동구 신암4동",
            "weather": "REH",
            "weather_value": 50
        }
    ]

    save_weather_info(json_simulation_data, "시뮬레이션용날씨.json")
    save_weather_info(json_simulation_data_good_weather, "시뮬레이션용날씨_좋은날.json")
    # HK Comment] 시뮬레이션 작업후  JSON 파일 저장할 것 (다른 이름으로)
    order_1 = input("1.비오는날 시뮬레이션(발코니창 제어)\n2.습한날 시뮬레이션(제습기 제어)\n3.건조한날 시뮬레이션(가습기 제어)\n\
4.상쾌한날 시뮬레이션\n동작입력 : ")
    if order_1 == '1' :
        window_control(json_simulation_data)

    elif order_1 == '2' :
        dehumidifier_control(json_simulation_data)

    elif order_1 == '3' :
        humidifier_control(json_simulation_data)

    elif order_1 == '4' :
        window_control(json_simulation_data_good_weather)
        dehumidifier_control(json_simulation_data_good_weather)
        humidifier_control(json_simulation_data_good_weather)


print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                                 - 김상엽 -")
jsonResult = []
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4) :
        simulation_mode()
    elif(menu_num == 5):
        break