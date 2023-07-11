class QuizGame:

    def __init__(self, question_set):
        self.question_number = 0
        self.score = 0
        self.question_set = question_set
        self.total_questions = len(question_set)

    def next_question_exists(self):
        return self.question_number < self.total_questions

    def get_new_question(self):
        current_question = self.question_set[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)? : ').lower()

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You are correct!")
            self.score += 1
        else:
            print("Sorry! You are wrong!")
            print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("")
