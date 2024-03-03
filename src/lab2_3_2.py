def put_on_board(n, w, h):
    note_size = w * h
    side_w = w
    side_h = h
    while (side_w * side_h) / note_size < n:
        if side_w + w > side_h + h:
            side_h += h
        else:
            side_w += w
    if side_w > side_h:
        result = side_w
    else:
        result = side_h
    return result
