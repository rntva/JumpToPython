# somefile = open("sample.txt", 'r')
# somefile1 = open("result.txt", 'w')
# token = 1
# x = ' '
# while x :
#     for x in somefile.readline() :
#         if token == 1 and x == '\t' :
#             # somefile1.write(x.replace('\t', '8888'))
#             somefile1.write("8888")
#         else : somefile1.write(x)
#         token = 0
#         if( x == '\n') :
#             token == 1
# somefile.close()
# somefile1.close()

# somefile = open("sample.txt", 'r')
# somefile1 = open("result.txt", 'w')
# token = 1
#
# for x in somefile.readlines() :
#     temp = list(x)
#     for y in temp :
#         if y == '\t' and token == 1 :
#             somefile1.write("8888")
#         else : somefile1.write(y)
#         token = 0
#         if y == '\n' : token = 1
#
# somefile.close()
# somefile1.close()

somefile = open("sample.txt", 'r')
somefile1 = open("result.txt", 'w')
token = 1

for x in somefile.readlines() :
    if x == '\t' and token == 1 :
        somefile1.write("8888")
    else : somefile1.write(x)
    token = 0
    if x == '\n' : token = 1

somefile.close()
somefile1.close()
