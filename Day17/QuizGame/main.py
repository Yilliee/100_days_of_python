from data import question_data
from question_model import Question
from quiz_brain import QuizGame

question_set = [Question(question["question"], question["correct_answer"]) for question in question_data["results"]]

quiz_game = QuizGame(question_set)

while quiz_game.next_question_exists():
    quiz_game.get_new_question()

print("The quiz has ended!")
print(f"Your final score is {quiz_game.score}/{quiz_game.total_questions}")