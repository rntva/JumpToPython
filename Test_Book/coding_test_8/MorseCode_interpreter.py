morsecode_dic \
    = { '.-' : 'A', '-...' : 'B', '-.-.' : 'C', '-..' : 'D', '.' : 'E', '--.' : 'G', \
        '....' : 'H', '..' : 'I', '.---' : 'J', '-.-' : 'K', '.-..' : 'L', '--' : 'M', \
        '-.' : 'N', '---' : 'O', '.--.' : 'P', '--.-' : 'Q', '.-.' : 'R', '...' : 'S', \
        '-' : 'T', '..-' : 'U', '...-' : 'V', '.--' : 'U', '-..-' : 'X', '-.--' : 'Y', \
        '--..' : 'Z'}

input_morse_code = input("모스 부호를 입력해 주십시오.\n:").split(' ')

# print(input_morse_code)

for x in input_morse_code :
    if x != '' : print(morsecode_dic.get(x), end = '')
    else : print(' ', end = '')

