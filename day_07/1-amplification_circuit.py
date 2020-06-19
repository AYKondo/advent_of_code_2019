def intcode(arr, code_position, number_input):
    if arr[code_position] == 99:
        return arr, number_input[1]

    opcode, parameters_mode = get_opcode(arr[code_position])
    parameters = get_parameters(arr, code_position, parameters_mode, opcode)

    if opcode == 1:
        arr[arr[code_position + 3]] = parameters[0] + parameters[1]
        position = code_position + 4
        
    elif opcode == 2:
        arr[arr[code_position + 3]] = parameters[0] * parameters[1]
        position = code_position + 4
        
    elif opcode == 3:
        if number_input[0] != -1:
            arr[arr[code_position + 1]] = number_input[0]
            number_input[0] = -1
        else:
            arr[arr[code_position + 1]] = number_input[1]

        position = code_position + 2
        
    elif opcode == 4:
        # print(arr[arr[code_position + 1]])
        position = code_position + 2
        number_input[1] = arr[arr[code_position + 1]]
        
    elif opcode == 5:
        if parameters[0] != 0:
            position = parameters[1]
        else:
            position = code_position + 3

    elif opcode == 6:
        if parameters[0] == 0:
            position = parameters[1]
        else:
            position = code_position + 3

    elif opcode == 7:
        if parameters[0] < parameters[1]:
            arr[arr[code_position + 3]] = 1
        else:
            arr[arr[code_position + 3]] = 0

        position = code_position + 4

    elif opcode == 8:
        if parameters[0] == parameters[1]:
            arr[arr[code_position + 3]] = 1
        else:
            arr[arr[code_position + 3]] = 0

        position = code_position + 4
        
    arr = intcode(arr, position, number_input)
    return arr

def get_opcode(code):
    if code < 10:
        return code, []
    else:
        opcode = code%10
        code_list = [int(x) for x in str(code)]
        code_list.pop(-1)
        code_list.pop(-1)
 
        return opcode, code_list

def get_parameters(arr,code_position, parameters_mode, opcode):
    parameters = list()

    if not parameters_mode:
        if opcode in [1, 2, 5, 6, 7, 8]:
            parameters.append(arr[arr[code_position + 1]])
            parameters.append(arr[arr[code_position + 2]])

    else:
        for x in range(len(parameters_mode)):
            x += 1
            if parameters_mode[-x] == 1:
                parameters.append(arr[code_position + x])
            else:
                parameters.append(arr[arr[code_position + x]])
        if len(parameters) < 2 and opcode != 4:
            parameters.append(arr[arr[code_position + 2]])

    return parameters

from itertools import permutations 
if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        arr = [int(x) for x in f.readline().split(',')]
        thruster = []
        for perm in permutations([0, 1, 2, 3, 4]):
            initial_input = 0
            for phase in perm:
                final_program, initial_input = intcode(arr, 0, [phase, initial_input])
            thruster.append(initial_input)

        print(sorted(thruster)[-1])