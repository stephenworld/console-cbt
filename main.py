from config import TERMINAL_WIDTH
from config import EXAM_QUESTIONS
from utils.welcome import welcome
from utils.clear_screen import clear_terminal
from utils.question_screen import question
from utils.actions import handle_next, handle_prev

clear_terminal()

success = welcome(TERMINAL_WIDTH)

if success:
    clear_terminal()

total_questions = len(EXAM_QUESTIONS)
all_answers = {q["id"]: q["answer"] for q in EXAM_QUESTIONS}

# State management: Store answers by question ID
user_answers = {q["id"]: None for q in EXAM_QUESTIONS}
current_question_index = 0
score = 0

while current_question_index < total_questions:
    q = EXAM_QUESTIONS[current_question_index]
    question_id = q["id"]
    current_answer = user_answers.get(question_id)
    
    # Keep showing question until valid action is taken
    while True:
        user_res = question(
            question = q["question"],
            options = q["options"],
            time_left= 1, # 1 minute countdown for each question
            q_num=q["id"],
            total_q=len(EXAM_QUESTIONS),
            current_answer=current_answer,
        )
        user_res = user_res.strip().upper() # Normalize input
        clear_terminal()

        # Handle Next action
        if user_res == "N":
            current_question_index = handle_next(current_question_index, total_questions)
            break
        
        # Handle Previous action
        elif user_res == "P":
            if current_question_index == 0:
                print("No previous question!")
                continue
            current_question_index = handle_prev(current_question_index)
            break
        
        # Handle Submit action
        elif user_res == "S":
            # Exit quiz and calculate score
            current_question_index = total_questions
            break

        # Handle Answer selection (1-4)
        elif user_res in ["A", "B", "C", "D"]:
            user_answers[question_id] = user_res
            current_question_index = handle_next(current_question_index, total_questions)
            break
        
        # Invalid input
        else:
            print("Invalid input. Please enter [P]revious, [N]ext, [S]ubmit, or [A-D] for Answers")


# Calculate score based on stored answers
attempted_questions = 0
score = 0

for question_id, user_answer in user_answers.items():
    if user_answer is not None:
        attempted_questions += 1
        if user_answer == all_answers[question_id]:
            score += 1

print("+" + "=" * (TERMINAL_WIDTH - 2) + "+")
print("|" + "".center(TERMINAL_WIDTH - 2) + "|")

if attempted_questions == 0:
    print("|" + "No answers submitted!".center(TERMINAL_WIDTH - 2) + "|")
else:
    percentage = (score / total_questions)* 100
    
    if percentage < 33:
        print("|" + "Poor Performance".center(TERMINAL_WIDTH - 2) + "|")
    elif percentage < 50:
        print("|" + "Below Average".center(TERMINAL_WIDTH - 2) + "|")
    elif percentage < 67:
        print("|" + "Awesome...".center(TERMINAL_WIDTH - 2) + "|")
    else:
        print("|" + "Excellent...".center(TERMINAL_WIDTH - 2) + "|")

print("|" + "".center(TERMINAL_WIDTH - 2) + "|")
print("|" + f"Attempted Questions: {attempted_questions}".center(TERMINAL_WIDTH-2) + "|")
print("|" + f"Total Questions: {total_questions}".center(TERMINAL_WIDTH-2) + "|")
print("|" + f"You scored {score} of {attempted_questions}".center(TERMINAL_WIDTH-2) + "|")

print("|" + "".center(TERMINAL_WIDTH - 2) + "|")
print("+" + "=" * (TERMINAL_WIDTH - 2) + "+")