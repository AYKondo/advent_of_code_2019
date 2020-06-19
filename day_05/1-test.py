def intcode(arr, code_position, number_input=0):
    if arr[code_position] == 99:
        return arr

    opcode, parameters_mode = get_opcode(arr[code_position])
    parameters = get_parameters(arr, code_position, parameters_mode, opcode)

    if opcode == 1:
        arr[arr[code_position+3]] = parameters[0] + parameters[1]
        plus_positions = 4
    elif opcode == 2:
        arr[arr[code_position+3]] = parameters[0] * parameters[1]
        plus_positions = 4
    elif opcode == 3:
        arr[arr[code_position+1]] = number_input
        plus_positions = 2
    elif opcode == 4:
        print(arr[arr[code_position+1]])
        plus_positions = 2

    arr = intcode(arr, code_position+plus_positions)
    return arr

def get_opcode(code):
    if code < 10:
        return code, []
    else:
        code_list = [int(x) for x in str(code)]
        code = str(code_list.pop(-2))
        code += str(code_list.pop(-1))
        return int(code), code_list

def get_parameters(arr,code_position, parameters_mode, opcode):
    parameters = list()

    if not parameters_mode:
        if opcode == 1 or opcode == 2:
            parameters.append(arr[arr[code_position+1]])
            parameters.append(arr[arr[code_position+2]])
    else:
        for x in range(len(parameters_mode)):
            if parameters_mode[-(x+1)] == 1:
                parameters.append(arr[code_position+x+1])
            else:
                parameters.append(arr[arr[code_position+x+1]])
        if len(parameters) < 2 and opcode != 4:
            parameters.append(arr[arr[code_position+2]])

    return parameters


if __name__ == "__main__":
    number_input = input("Give me a number: ")
    with open('./input.txt', 'r') as f:
        arr = [int(x) for x in f.readline().split(',')]
        arr = intcode(arr, 0, int(number_input))
