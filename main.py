from config import TERMINAL_WIDTH
from config import EXAM_QUESTIONS
from utils.welcome import welcome
from utils.clear_screen import clear_terminal
from utils.question_screen import question

success = welcome(TERMINAL_WIDTH)

if success:
    clear_terminal()
total_questions = len(EXAM_QUESTIONS)
current_question = 0
userAnswer = []

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

    userAnswer.append({f"Question {current_question}: {user_res}"})
    clear_terminal()


print(userAnswer)