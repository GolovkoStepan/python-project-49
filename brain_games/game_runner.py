from brain_games.cli import (
    congratulation_message,
    correct_answer_message,
    get_user_answer,
    question_message,
    task_message,
    welcome_user,
    wrong_answer_message,
)


def run_game(task_description, make_question_function):
    user_name = welcome_user()
    task_message(task_description)

    for _ in range(3):
        question, correct_answer = make_question_function()

        question_message(question)
        user_answer = get_user_answer()

        if user_answer == correct_answer:
            correct_answer_message()
        else:
            wrong_answer_message(user_name, user_answer, correct_answer)
            return
    
    congratulation_message(user_name)
