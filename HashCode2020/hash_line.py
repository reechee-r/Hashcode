# files = open(b'a_example.in')
# files = open(b'b_small.in')
# with open('c_medium.in','r') as files:
#     fileslines = files.readlines()
#     setters = fileslines[0]
#     #select last item on the list and strip out newline characters
#     inputvalues = fileslines[1:][0].strip('\n')
#     setters.strip('\n').split(' ')

#this function parsers and returns all vaules in a dictionary
def parser():
    with open('c_medium.in','r') as files:
            fileslines = files.readlines()
            setters = fileslines[0].strip('\n').split(' ')
            #select last item on the list and strip out newline characters
            datavalues = fileslines[1:][0].strip('\n')
            maximumslices = int(setters[0])
            typesofpizza = int(setters[1])
            post = {
                "datavalues": datavalues,
                "maximumslices": maximumslices,
                "typesofpizza": typesofpizza
            }
    return post
olo = parser()

