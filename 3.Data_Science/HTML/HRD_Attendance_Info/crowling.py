attendance_info = []
append_token = 0
now_start = 1
numbering = 1
init_token = 0
late = 0
absence = 0

starting_date = input("수업 시작 날짜를 입력해 주십시오.\n(e.g. 2017-11-20) : ")
print("훈련과정 상세출결현황 복붙하기.(Ctrl+A & Ctrl+C & Ctrl+V)")

while 1 :
    temp = input()
    if temp == '' and append_token == 0 : append_token = 1
    elif temp == '' and append_token == 1 : break
    attendance_info.append(temp)
    temp = ''

monthly_attending_info = []
for x in attendance_info :
    if now_start == 1 :
            monthly_attending_info.append([x.split('\t')[0]] + [x.split('\t')[-1]])
    elif x.split('\t')[0] == starting_date :
        monthly_attending_info.append([x.split('\t')[0]] + [x.split('\t')[-1]])
        now_start = 1

for x in monthly_attending_info :
    if x[1] == "지각" and late <= 1 : late += 1
    elif x[1] == "지각" and late == 2 :
        late = 0
        absence += 1
    elif x[1] == "결석" : absence += 1
print("%d회차 교육결과 => 결석 : %d\t지각 : %d" % (numbering, absence, late))
