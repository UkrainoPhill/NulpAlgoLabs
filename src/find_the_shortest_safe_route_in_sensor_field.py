def read_input(input_directory):
    with open(input_directory, "r") as input_file:
        matrix = []
        for line in input_file:
            row = list(map(int, line.split(", ")))
            matrix.append(row)
        print(matrix)
    return matrix


def check_for_zeros(matrix, row_number, column_number):
    for row, column in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= row_number + row < len(matrix) and 0 <= column_number + column < len(matrix[0]) and matrix[row_number + row][column_number + column] == 0:
            return True
    return False


def write_output(output_directory, shortest_route):
    with open(output_directory, "w") as output_file:
        output_file.write(str(shortest_route))


def get_path(previous_vertex, start_p):
    path = 0
    current_vertex = start_p
    while current_vertex is not None:
        path += 1
        current_vertex = previous_vertex[current_vertex]
    return path


def find_the_shortest_safe_route_in_sensor_field(matrix):
    print(matrix)
    shortest_route = float("inf")
    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            path_len = bfs((i, 0), matrix)
            if path_len < shortest_route and path_len != -1:
                shortest_route = path_len
    if shortest_route == float("inf"):
        return -1
    return shortest_route


def bfs(start_p, matrix):
    previous_vertex = {start_p: None}
    queue = [start_p]
    visited = set()
    while queue:
        current_vertex = queue.pop(0)
        if current_vertex[1] == len(matrix[0]) - 1:
            return get_path(previous_vertex, current_vertex)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for row, col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row = current_vertex[0] + row
            new_col = current_vertex[1] + col
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == 1 and (new_row, new_col) not in visited and not check_for_zeros(matrix, new_row, new_col):
                queue.append((new_row, new_col))
                previous_vertex[(new_row, new_col)] = current_vertex

    return -1


def main(input_directory, output_directory):
    matrix = read_input(input_directory)
    shortest_route = find_the_shortest_safe_route_in_sensor_field(matrix)
    write_output(output_directory, shortest_route)


main("../test/resources/input.txt", "../test/resources/output.txt")