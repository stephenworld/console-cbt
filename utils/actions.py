def handle_next(current_index, total_questions):
    if current_index < total_questions - 1:
        return current_index + 1
    else:
        return current_index

def handle_prev(current_index):
    if current_index > 0:
        return current_index - 1
    else:
        return current_index

