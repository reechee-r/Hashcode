def ReadInputFile(file:int)->EvenMorePizza:
    """Read the file and return the class EvenMorePizza"""
    self.files = ('a_example.in','b_little_bit_of_everything.in', 'c_many_ingredients.in','d_many_pizzas.in','e_many_teams.in')
    
    EvenMorePizza temporalValue
    
    file = open(files[file])#open the file
    data = doc.Read().strip(' ,\n').split('\n')
    file.close()#close the file
    #set the title of the command
    data_head = data[0].strip(' ,\n').split(' ')
    temporalValue.AvailablePizza = int(data_head[0])
    temporalValue.Team2ppl = int(data_head[1])
    temporalValue.Team3ppl = int(data_head[2])
    temporalValue.Team4ppl = int(data_head[3])
    #set the other ingredients
    count = 0
    for a in data[1:]:
        x = a.strip(' ,\n').split(' ')
        temporalValue.ingredients[count] = x[1:]
        count += 1

#print the results
def WriteOutputFile(output:Results):
    with open('result.txt','w') as solution:
        Results solution_result
        print(solution_result.teams_delivered, file=solution)
        for val in solution_result.result:
            print('val',solution_result_result[val])


#making variable for each value
class EvenMorePizza:
    """Store the variables in a class"""
    int self.AvailablePizza
    int self.Team2ppl
    int self.Team3ppl
    int self.Team4ppl

    self.ingredients[][]

class Results:
    """Store the results"""
    int self.teams_delivered
    dict self.result

if __main__:
    ReadInputFile(" ")
