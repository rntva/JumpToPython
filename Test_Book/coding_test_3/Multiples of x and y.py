import time
you_cannot_excape_this_loof = '''\
장비를 정지합니다.
정지하겠습니다.
안 되잖아?
어? 저, 정지가 안 돼. 정지시킬 수가 없어
안-돼~~~!
이런 일이 일어날 것 같은 조짐을 느꼈지.
하지만 행정관이 내 말을 듣지 않았어.
오늘은 중요한 날이야, 프리맨?
모든게 제대로 되어 가는군.
난 더 이상 감당할 수 없어.
이런걸 전에 본 적이 있나?
안돼, 그쪽으로 가지마.
난 정말 모르겠어.
여기서 과연 나갈 수가 있을까?
난 여기서 빠져나가야 되겠어.
아하이구 맙소사, 우린 인제 죽었어.
안돼! 죽고 싶지 않아.
이건 미친 짓이야, 나는 여기서 나가겠어.
안 되잖아?
으아아아아아아아~\
'''
while 1 :
    try :
        range_a, range_b = input("범위를 지정해 주세요.(공백으로 구분) : ").split(' ')
        mul_a, nul_b = input("배수 X,Y를 지정해 주세요.(공백으로 구분) : ").split(' ')
        range_a = int(range_a)
        range_b = int(range_b)
        result = 0
        if range_a < 0 or range_b < 0 :
            print("Nope. 자연수만 받습니다.")
        else :
            for x in range(range_a,range_b) :
                if x % 3 == 0 or x % 5 == 0 :
                    result += x
            print("%d부터 %d까지 3과 5의 배수의 합 : %d\n(문자를 입력하시오.)" %(range_a, range_b, result))
    except :
        for x in you_cannot_excape_this_loof :
            print(x, end='')
            if x == '\n' :
                time.sleep(2)
        print("\n\nYou can not expcase this loof, until you die.\n")
