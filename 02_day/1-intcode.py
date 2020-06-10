def intcode(arr, code_position):
    if arr[code_position] not in [1, 2, 99]:
        return "ERROR!"
    elif arr[code_position] == 99:
        return arr
    elif arr[code_position] == 1:
        arr[arr[code_position+3]] = arr[arr[code_position+1]] + arr[arr[code_position+2]]
    elif arr[code_position] == 2:
        arr[arr[code_position+3]] = arr[arr[code_position+1]] * arr[arr[code_position+2]]

    arr = intcode(arr, code_position+4)
    return arr

if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        arr = [int(x) for x in f.readline().split(',')]
        arr[1] = 12
        arr[2] = 2
        arr = intcode(arr, 0)
        print(arr[0])