class QuizBrain:

    def __init__(self, q):
        self.question_number = 0
        self.question_list = q
        self.score = 0

    def next_question(self):
        var = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f'Q.{self.question_number}: {var.text} (True/False)?: ')
        self.check_answer(u_answer, var.answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, u_answer, correct):
        if u_answer.lower() == correct.lower():
            print("You got it right")
            self.score += 1
            print(f"You current score is: {self.score}/{self.question_number}")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct}.")
        print("\n")
