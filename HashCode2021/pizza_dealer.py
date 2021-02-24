filename = 'HashCode2021/a_example.in'

with open(filename, 'r') as file:
    data = file.read().strip(' ,\n').split('\n')
    first_line = data[0].strip(' ,\n').split(' ')
    first_line = [int(i) for i in first_line]


    # print(first_line)
    