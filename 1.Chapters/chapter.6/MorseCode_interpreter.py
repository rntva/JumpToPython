morsecode_dic \
    = { '.-' : 'A', '-...' : 'B', '-.-.' : 'C', '-..' : 'D', '.' : 'E', '--.' : 'G', \
        '....' : 'H', '..' : 'I', '.---' : 'J', '-.-' : 'K', '.-..' : 'L', '--' : 'M', \
        '-.' : 'N', '---' : 'O', '.--.' : 'P', '--.-' : 'Q', '.-.' : 'R', '...' : 'S', \
        '-' : 'T', '..-' : 'U', '...-' : 'V', '.--' : 'U', '-..-' : 'X', '-.--' : 'Y', \
        '--..' : 'Z' }

blank = ' '

# reslut = ""
# def interpreting_morsecode(str) :
#     global morsecode_dic
#     return morsecode_dic.get(str)
#
# morse_input = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
# list_morse  = morse_input.split(' ')
# for x in list_morse :
#     if x != '' : reslut += interpreting_morsecode(x)
#     else : reslut += ' '
# print(reslut)

def interpreting_morsecode(str) :
    global morsecode_dic
    if str != '' : return morsecode_dic.get(str)
    else : return blank

morse_input = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"

list_morse  = morse_input.split(' ')

for x in list_morse :
    print(interpreting_morsecode(x), end='')

