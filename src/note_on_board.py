def put_on_board(number_notes, note_width, note_height):
    note_area = note_width * note_height
    board_width = note_width
    board_height = note_height
    while (board_width * board_height) / note_area < number_notes:
        if board_width + note_width > board_height + note_height:
            board_height += note_height
        else:
            board_width += note_width
    if board_width > board_height:
        result = board_width
    else:
        result = board_height
    return result
