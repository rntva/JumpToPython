def get_total_pages(m, n) :
    if m % n == 0 and (m / n) > 0 : return m / n
    else : return m / n + 1

file_1 = open("condition.txt", 'r')
for x in range(5) :
    temp = file_1.readline().split(' ')
    try :
        m = int(temp[0])
        n = int(temp[1])
    except : continue
    if m == 0 or n == 0 : continue
    print("게시물 총 건수 : %d, 한 페이지에 보여줄 게시물 수 : %d, 총 페이지수 : %d"\
%(m, n, get_total_pages(m,n)))