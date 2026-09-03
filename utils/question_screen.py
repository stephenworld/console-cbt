def question(question, time_left, q_num, total_q, options, current_answer=None):
    width = 60
    
    header_text = f"QUESTION: {q_num}/{total_q} | TIME LEFT: {time_left*60} seconds"
    
    # 1. Print Top Border and Header
    print("=" * width)
    print(header_text.center(width))
    print("=" * width)
    print("".center(width))

    # 2. Print Question Info
    print(f"QUESTION {q_num}\n{question}")
    print()

    # 3. Showing options
    for option in options:
        print(f"{option}")
    print()
    
    # 4. Show current answer if one exists
    if current_answer is not None:
        print(f"[Current Answer: {current_answer}]".center(width))
        print()
    
    # 5. Print Bottom Navigation and Borders
    print("=" * width)
    print("[P]revious  |  [N]ext  |  [S]ubmit  |  [A-D]Answer".center(width))
    print("=" * width)
    
    # 6. Take User Input at the very bottom
    answer = input("\n Your Answer (or action): ")
    return answer
