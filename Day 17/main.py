from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank=[]
for question in question_data:
    question=Question(question["question"],question["correct_answer"])
    question_bank.append(question)

quiz=Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

