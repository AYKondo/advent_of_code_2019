def get_positions(commands):
    x, y = 0, 0
    steps = 0
    steps_map = {}
    positions = set()
    for i in range(len(commands)):
        for _ in range(int(commands[i][1:])):
            direction = commands[i][0]
            
            if   direction == "R":
                x +=1
            elif direction == "L":
                x -=1
            elif direction == "D":
                y -=1
            elif direction == "U":
                y +=1
                
            steps += 1
            steps_map[f"{x},{y}"] = steps
            positions.add((x, y))

    return positions, steps_map


if __name__ == "__main__":
    wire_number = 1
    positions = []
    steps = {}
    crossings = []
    i = 0
    with open('./input.txt', 'r') as f:
        for line in f:
            commands = line.split(',')
            # Calculate all positions from all commands
            # Calculate all steps for each position
            command_positions, wire_steps = get_positions(commands)
            # Add all positions to an array, use later to intersect
            positions.append(command_positions)
            # Add all mapping steps to dict
            steps[i] = wire_steps
            i += 1

        # Intersect from two wires
        crossings = positions[0].intersection(positions[1])

    cross_steps = []
    for cross in crossings:
        wire_steps = 0
        # For each cross sum up the steps from all lines(wires)
        for wire in range(i):
            wire_steps += steps[wire][f"{cross[0]},{cross[1]}"]
        # Add the sum up from each cross
        cross_steps.append(wire_steps)

    # Get the fewest steps
    print(min(cross_steps))
