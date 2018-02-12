def converting(target, target_division) :
    select_number = "0123456789ABCDEF"
    result_number = select_number[target % target_division]
    while 1 :
            target /= target_division
            target = int(target)
            if target == 0 :
                for x in range(len(result_number)) : print(result_number[len(result_number)-1-x], end = '')
                break
                # result_number = list(result_number)
                # result_number.reverse()
                # return result_number
            result_number += select_number[target % target_division]
    print()
converting(233, 2)
converting(233, 8)
converting(233, 16)