from config import TERMINAL_WIDTH
from config import EXAM_QUESTIONS
from utils.welcome import welcome
from utils.clear_screen import clear_terminal
from utils.question_screen import question
clear_terminal()
success = welcome(TERMINAL_WIDTH)

if success:
    clear_terminal()
total_questions = len(EXAM_QUESTIONS)
all_answers = [q["answer"] for q in EXAM_QUESTIONS]

current_question = 0
userAnswer = []
score = 0

for q in EXAM_QUESTIONS:
    user_res = question(
        question = q["question"],
        options = q["options"],
        time_left="14:59",
        q_num=q["id"],
        total_q=len(EXAM_QUESTIONS),
    )
    current_question += 1
    clear_terminal()

    valid_input = ["1", "2", "3", "4"]
    while user_res not in valid_input:
        clear_terminal()
        print("Invalid answer, try again")
        user_res = question(
            question = q["question"],
            options = q["options"],
            time_left="14:59",
            q_num=q["id"],
            total_q=len(EXAM_QUESTIONS),
        )

    userAnswer.append(user_res)
    clear_terminal()


for idx in range(total_questions):
    if userAnswer[idx] == all_answers[idx]:
        score += 1

print("+" + "=" * (TERMINAL_WIDTH - 2) + "+")
print("|" + "".center(TERMINAL_WIDTH - 2) + "|")

if score < 1/3:
    print("|" + "Poor Performance".center(TERMINAL_WIDTH - 2) + "|")
elif score < 1/2:
    print("|" + "Below Average".center(TERMINAL_WIDTH - 2) + "|")
elif score < 2/3:
    print("|" + "Awesome...".center(TERMINAL_WIDTH - 2) + "|")
else:
    print("|" + "Excellent...".center(TERMINAL_WIDTH - 2) + "|")

print("|" + f"You scored {score} of {total_questions}".center(TERMINAL_WIDTH-2) + "|")

print("|" + "".center(TERMINAL_WIDTH - 2) + "|")
print("+" + "=" * (TERMINAL_WIDTH - 2) + "+")