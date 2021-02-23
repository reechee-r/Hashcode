#----------------------------------
#array of the file names for easy accessiblity
#----------------------------------

files = ('a_example.in','b_little_bit_of_everything.in', 'c_many_ingredients.in','d_many_pizzas.in','e_many_teams.in')


#--------------------------------------
#information about the data sets in general
#----------------------------------------

def generalInformation(x):
    """tells you all you need to know about the file with number 'x'"""
    titleInformation(x)
    dataInformation(x)

def titleInformation(x):
    """print the description for the heading(first line)"""

    print(50*'-', '\n', 50*'-')

    if x>=6:
        print('the number must be between 1 and 5')
        return

    print('file number: ', x, '\n')
    print('file name: ', files[x-1], '\n')
    numbers = processFirstLine(getFirstLine(x))
    print('There are ', numbers[1], ' two man team(s): this gives a total of :', int(numbers[1])*2, 'people')
    print('There are ', numbers[2], ' three man team(s): this gives a total of :', int(numbers[2])*3, 'people')
    print('There are ', numbers[3], ' four man team(s): this gives a total of :', int(numbers[3])*4, 'people')
    print(20*'-','\n\n',)
    totalPeople = (int(numbers[1])*2) + (int(numbers[2])*3) + (int(numbers[3])*4)
    totalTeams = int(numbers[1]) + int(numbers[2]) + int(numbers[3])

    print('The total number of pizzas is: ', numbers[0], '\n')
    print('The total number of teams are: ', totalTeams, '\n')
    print('The total number of people are: ', totalPeople)
    print(50*'-', '\n', 50*'-')

def dataInformation(x):
    """print the information and description of all the data files"""
    print(50*'-', '\n', 50*'-')

    if x>=6:
        print('the number must be between 1 and 5')
        return
    
    print('file number: ', x, '\n')
    print('file name: ', files[x-1], '\n')

    print('number of pizzas: ', getFirstLine(x)[0], '\n')
    various = getVariety(x)
    print('number of ingredients: ', len(various), '\n')

    print('------ingredient names and number of occurence---------\n')
    for val in various:
        print(val, '\t:', various[val], '\n')

    print(50*'-', '\n', 50*'-')    
    

    
#-----------------------------------------------
#this is for processing the title of the data set
#-----------------------------------------------

def printFile(x):
    """print all the characters in the document"""
    x = x-1
    test = open(files[x])
    for line in test:
        print(line)
    test.close()

def getFirstLine(x):
    """get the first line"""
    x = x-1
    test = open(files[x])
    return test.readline().strip(' ,\n')

def processFirstLine(x):
    """work on the values of x """
    numbers = (x.split(' '))
    return numbers


#----------------------------------------
#this is for processing the rest of the data sets
#------------------------------------------

def getOtherLines(x):
    """get a list of the remaining files"""
    x = x-1
    test = open(files[x])
    lineCount = 0;
    pizzas = test.read().strip(' ,\n').split('\n')
    pizzas.pop(0)
    test.close()

    sortedPizzas = list()
    
    for x in pizzas:
        sortedPizzas.append(x.split(' '))
        
    return sortedPizzas


def getVariety(x):
    various = dict()
    lists = getOtherLines(x)

    for val in lists:
        for i in range(1, len(val)):

            if val[i] in various:
                various[val[i]] += 1
            else:
                various[val[i]] = 1
                

    return various


#------------------------------------------
#using the functions created above to make some projects
#-----------------------------------------

x = int(input('Enter the file number to print: '))

generalInformation(x)
