import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for q_a in data.question_data['results']:
    question_bank.append(Question(q_a['question'], q_a['correct_answer']))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've complete the quiz \nYour final score was: {quiz.score}/{quiz.question_number}")

