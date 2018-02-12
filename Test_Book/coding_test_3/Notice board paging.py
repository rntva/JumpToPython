while 1:
    try :
        Total_item, Items_per_page= input("총 건수와 페이지당 게시물 수 입력(공백으로 구분) : ").split(' ')
        Total_item = int(Total_item)
        Items_per_page = int(Items_per_page)
        if Total_item < 0 or Items_per_page <= 0 :
            print("Nope. 웬만하면 자연수만 넣어라.")
            continue
        else :
            if Total_item % Items_per_page != 0 :
                adder = 1
            else : adder = 0
            print("필요한 총 페이지 수는 %d이다" %(Total_item / Items_per_page + adder) )
    except :
        print("하지 싫으면 말어라")
        break
