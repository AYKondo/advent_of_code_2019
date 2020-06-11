def calc_manhattan_distance(crossings):
    distances = []
    for cross in crossings:
        distances.append(abs(cross[0]) + abs(cross[1]))
    return distances

def get_positions(commands):
    x, y = 0, 0   
    positions = set()

    for i in range(len(commands)):
        for _ in range(int(commands[i][1:])):
            direction = commands[i][0]
            
            if   direction == "R":
                x +=1
            elif direction == "L":
                x -=1
            elif direction == "D":
                y +=1
            elif direction == "U":
                y -=1
            
            positions.add((x, y))
    
    return positions


if __name__ == "__main__":
    wire_number = 1
    positions = []
    with open('./input.txt', 'r') as f:
        for line in f:
            commands = line.split(',')
            positions.append(get_positions(commands))
    
    crossings = positions[0].intersection(positions[1])
    manhattans_distances = calc_manhattan_distance(crossings)
    print(min(manhattans_distances))