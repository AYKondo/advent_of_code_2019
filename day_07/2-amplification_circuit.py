def intcode(arr, code_position, phase_settings, phase_count):
    if arr[code_position] == 99:
        if phase_count == 4:
            return phase_settings[0]["input"][-1]

        return 0

    opcode, parameters_mode = get_opcode(arr[code_position])
    parameters = get_parameters(arr, code_position, parameters_mode, opcode)

    if opcode == 1:
        arr[arr[code_position + 3]] = parameters[0] + parameters[1]
        position = code_position + 4
        
    elif opcode == 2:
        arr[arr[code_position + 3]] = parameters[0] * parameters[1]
        position = code_position + 4
        
    elif opcode == 3:
        try:
            input_position = phase_settings[phase_count]["count"]
            arr[arr[code_position + 1]] = phase_settings[phase_count]['input'][input_position]
            phase_settings[phase_count]["count"] += 1
        except:
            phase_settings[phase_count]['count'] = 0
            return 0

        position = code_position + 2
        
    elif opcode == 4:
        code_out = arr[arr[code_position + 1]]
        if phase_count == 4:
            if code_out in phase_settings[0]['input']:
                pass
            else:
                phase_settings[0]['input'].append(code_out)
        else:
            if code_out in phase_settings[phase_count+1]['input']:
                pass
            else:
                phase_settings[phase_count+1]['input'].append(code_out)

        position = code_position + 2
        
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
        
    arr = intcode(arr, position, phase_settings, phase_count)
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
        thruster = []
        for perm in permutations([5, 6, 7, 8, 9]):
            if perm in [(5, 7, 8, 6, 9), (5, 9, 8, 7, 6), (6, 8, 5, 7, 9), (6, 8, 5, 9, 7), (6, 8, 7, 5, 9), (6, 8, 7, 9, 5), (6, 8, 9, 5, 7), (6, 8, 9, 7, 5), (6, 9, 5, 8, 7),
            (7, 5, 8, 6, 9),(7, 8, 5, 6, 9), (7, 8, 5, 9, 6), (7, 8, 6, 5, 9), (7, 8, 6, 9, 5),(7, 8, 9, 5, 6),(7, 8, 9, 6, 5), (7, 9, 8, 6, 5), (9, 5, 7, 8, 6),
            (9, 5, 8, 7, 6), (9, 6, 7, 8, 5), (9, 7, 5, 8, 6),(9, 7, 6, 8, 5), (9, 7, 8, 6, 5),(9, 8, 6, 7, 5),(9, 8, 7, 6, 5)]:
                continue
            initial_input = 0
            phase_settings = []
            count = 0
            exit_code = 0
            for phase in perm:
                phase_settings.append({
                    "input": [phase],
                    "count": 0})

            phase_settings[0]['input'].append(0)
            while True:
                with open('./input.txt', 'r') as f:
                    arr = [int(x) for x in f.readline().split(',')]
                    exit_code = intcode(arr, 0, phase_settings, count)
                    f.close()

                if count == 4:
                    count = 0
                else:
                    count += 1
                
                if exit_code != 0:
                    thruster.append(exit_code)
                    break
        
        print(sorted(thruster)[-1])
