filename = 'HashCode2021/a_example.in'

with open(filename, 'r') as file:
    data = file.read().strip(' ,\n').split('\n')
    first_line = data[0].strip(' ,\n').split(' ')
    first_line = [int(i) for i in first_line]

    pizza_list = []

    pizza_data = data[1:]

    for v in range(len(pizza_data)):
        x = data[v+1].strip(' ,\n').split(' ')
        pizza_list.append(set(x[1:]))

    print(first_line)    
    print(pizza_list)