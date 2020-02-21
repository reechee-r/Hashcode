import itertools
# filename = open('a_example.in')
#this function parsers and returns all vaules in a dictionary
# filename = 'a_example.in'
# filename = 'b_small.in'
# filename = 'c_medium.in'
filename = 'd_quite_big.in'
# filename = 'e_also_big.in'

def parser(filename):
    with open(filename,'r') as files:
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
post = parser(filename)

string = post['datavalues']
maximumslices = post['maximumslices']
# typesofpizza = post['typesofpizza']
typesofpizza = 1990

maximumcombination = []
#this function converts strings to list
# def string2list(string, maximumslices): 
import pdb; pdb.set_trace()

print('starting computation......')
for pizzas in range(typesofpizza).__reversed__():
    print('computing for ', pizzas)
    # answer = [listofchops.index(i) for i in maximumcombination]
    # print(maximumcombination, '===>',answer, sum(maximumcombination))
    listofchops = [int(i) for i in string.split(' ')]
    soupofCombinations = itertools.combinations(listofchops, pizzas)
    # print([i for i in listCombinations])
    for setofcombinations in soupofCombinations: 
        # print(setofcombinations)
        currentcombination = sum(setofcombinations)
        print('checking for',currentcombination)
        if currentcombination == maximumslices:
        # if currentcombination <= maximumslices:
        #     if currentcombination >= sum(maximumcombination):
            maximumcombination = setofcombinations
            print(maximumcombination)
    print(pizzas, 'the computation has ended')
# string2list(string, maximumslices)
answer = [listofchops.index(i) for i in maximumcombination]
# for i in maximumcombination:
#     print(listofchops.index(i))
# indexofmaximumcombination = maximumcombination[0]

print(maximumcombination, '===>',answer, sum(maximumcombination))



    





