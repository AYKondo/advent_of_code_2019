def calculate_fuel(mass):
    '''Calculate fuel divide mass by 3, round down, then subtract 2'''
    total_fuel = 0
    while True:
        mass = int(mass/3) - 2
        if mass > 0:
            total_fuel += mass
        else:
            break
    return total_fuel

if __name__ == "__main__":
    sum_fuel = 0
    with open('./input.txt', 'r') as f:
        for line in f:
            sum_fuel += calculate_fuel(int(line))
    print(sum_fuel)