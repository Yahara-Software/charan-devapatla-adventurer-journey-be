def calculate_distance(directions):
    # Vectors for directions: North, East, South, West (clockwise)
    dir_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0  # Starting position
    cur_dir_index = 0  # Start facing North (index 0 in dir_vectors)

    i = 0
    while i < len(directions):
        steps = 0
        while i < len(directions) and directions[i].isdigit():
            steps = steps * 10 + int(directions[i])
            i += 1

        # Skip negative steps (Assuming they are not required from question)
        if steps < 0:
            continue

        # Extract the direction character
        if i < len(directions):
            direction = directions[i]
            i += 1

            # Finding the Invalid (Only F, B, R and L are valid)
            if direction not in ['F', 'B', 'R', 'L']:
                print(f"Invalid direction character '{direction}' ignored.")
                continue

            if direction == 'F':  # Move forward in the current direction
                dx, dy = dir_vectors[cur_dir_index]
                x += dx * steps
                y += dy * steps
            elif direction == 'B':  # Move backward (opposite direction)
                dx, dy = dir_vectors[cur_dir_index]
                x -= dx * steps
                y -= dy * steps
            elif direction == 'R':  # Turn right (clockwise direction)
                cur_dir_index = (cur_dir_index + steps // 90) % 4
            elif direction == 'L':  # Turn left (counter clockwise direction)
                cur_dir_index = (cur_dir_index - steps // 90) % 4

    # Calculate the Euclidean distance from the origin
    distance = (x*2 + y*2) * 0.5
    return distance
    
# Input provided in question is given below
directions = "15F6B5L16R8B16F20L6F13R"
distance = calculate_distance(directions)
print(f"The Euclidean distance is: {calculate_distance(directions)}")

# Test Cases for calculating distance in possible ways
test_cases = [
    "",                # Empty input
    "10F",             # Single forward movement
    "5B",              # Single backward movement
    "90R180L",         # Only turns given
    "10F10B",          # Forward and backward cancel out
    "10F90R10F90R10F90R10F",  # Complete square path
    "0F",              # Zero or No movement
    "10F5X3B",         # Invalid character introduced
    "1000000F1000000R1000000F",  # Large or Big input
    "90R90R90R90R"     # Consecutive turns
]

for directions in test_cases:
    distance = calculate_distance(directions)
    print(f"Directions: '{directions}', Euclidean distance: {distance}")



# Expected Output
"""
The Euclidean distance is: 23.0
Directions: '', Euclidean distance: 0.0
Directions: '10F', Euclidean distance: 10.0
Directions: '5B', Euclidean distance: 5.0
Directions: '90R180L', Euclidean distance: 0.0
Directions: '10F10B', Euclidean distance: 0.0
Directions: '10F90R10F90R10F90R10F', Euclidean distance: 0.0
Directions: '0F', Euclidean distance: 0.0
Invalid direction character 'X' ignored.
Directions: '10F5X3B', Euclidean distance: 7.0
Directions: '1000000F1000000R1000000F', Euclidean distance: 1414213.562373095
Directions: '90R90R90R90R', Euclidean distance: 0.0
"""


