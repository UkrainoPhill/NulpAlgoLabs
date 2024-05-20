def calculate_distance(gap_measure: int, height_difference: int) -> float:
    """
    Calculate the distance between two poles given the gap measure and the height difference.
    :param gap_measure: The width of the gap between the poles.
    :param height_difference: The difference in height between two poles.
    :return: The distance between the two poles.
    """
    return (gap_measure ** 2 + height_difference ** 2) ** 0.5


def define_max_wire_length(gap_measure: int, pole_max_heights: list[int]) -> float:
    """
    Compute the maximum length of wire needed to connect poles in the village.
    :param gap_measure: The width of the gap between the poles.
    :param pole_max_heights: A list of integers representing the maximum possible height of each pole.
    :return: The maximum length of wire needed to connect the poles.
    """
    max_path_to_top = 0
    max_path_to_bottom = 0
    current_pole_index = 0
    while current_pole_index < len(pole_max_heights) - 1:
        height_difference = abs(pole_max_heights[current_pole_index] - pole_max_heights[current_pole_index + 1])
        top_to_bottom = max_path_to_top + calculate_distance(gap_measure, pole_max_heights[current_pole_index] - 1)
        bottom_to_bottom = max_path_to_bottom + gap_measure
        bottom_to_top = max_path_to_bottom + calculate_distance(gap_measure, pole_max_heights[current_pole_index + 1] - 1)
        top_to_top = max_path_to_top + calculate_distance(gap_measure, height_difference)
        max_path_to_top = max(bottom_to_top, top_to_top)
        max_path_to_bottom = max(bottom_to_bottom, top_to_bottom)
        current_pole_index += 1
    return max(max_path_to_top, max_path_to_bottom)