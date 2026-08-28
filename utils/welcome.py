def welcome(TERMINAL_WIDTH):
    title = "COMPUTER BASED TEST PORTAL"
    subject = "Subject: General Science"
    timer =  "Time Allowed: 45 Minutes"
    instruction = "Press [ENTER] to begin"

    print("+" + "=" * (TERMINAL_WIDTH - 2) + "+")
    print("|" + "".center(TERMINAL_WIDTH - 2) + "|")

    print("|" + title.center(TERMINAL_WIDTH - 2) + "|")
    print("|" + subject.center(TERMINAL_WIDTH - 2) + "|")
    print("|" + timer.center(TERMINAL_WIDTH - 2) + "|")

    print("|" + "".center(TERMINAL_WIDTH - 2) + "|")
    print("|" + instruction.center(TERMINAL_WIDTH - 2) + "|")
    print("+" + "=" * (TERMINAL_WIDTH - 2) + "+")

    input()

    return True

