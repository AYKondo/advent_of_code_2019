def calculate_passwords(input):
    n_passwords = 0
    for number in range(input[0], input[1]+1):
        arr = [int(x) for x in str(number)]
        doubles = False
        increase = True
        for value in range(len(arr)):
            if value == 0:
                continue
            elif arr[value] < arr[value-1]:
                increase = False
                break
            elif arr[value] == arr[value-1]:
                doubles = True
        if doubles and increase:
            n_passwords += 1
    return n_passwords



if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        input = f.readline().split('-')
        input = [int(x) for x in input]
        number_of_pass = calculate_passwords(input)
        print(number_of_pass)