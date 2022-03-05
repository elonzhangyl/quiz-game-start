from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
new_question_data = question_data["results"]
for question_item in new_question_data:
    # question_text = question["text"]
    # question_answer = question["answer"]
    question = Question(question_item["question"], question_item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()

print("You've complete the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
