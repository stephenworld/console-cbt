def question(question, time_left, q_num, total_q, options):
    width = 60
    
    header_text = f"QUESTION: {q_num}/{total_q} | TIME LEFT: {time_left}"
    
    # 1. Print Top Border and Header
    print("=" * width)
    print(header_text.center(width))
    print("=" * width)
    print("".center(width))

    # 2. Print Question Info
    print(f"QUESTION {q_num}\n{question}")
    print()

    # 3. SHowing options
    for option in options:
        print(f"{option}")
    print()
    
    # 4. Print Bottom Navigation and Borders
    print("=" * width)
    print("[P]revious  |  [N]ext  |  [S]ubmit  |  [1-4]Answer".center(width))
    print("=" * width)
    
    # 5. Take User Input at the very bottom
    answer = input("\n Your Answer (or action): ")
    return answer
