from quize_model import  Question
from data import question_data
from quize_brain import QuizeBrain
from ui import QuizInterface

question_bank = [

]
for key in question_data:
   question = key["text"]
   answer = key["answer"]
   appending = Question(question, answer)
   question_bank.append(appending)

quiz = QuizeBrain(question_bank)
quiz_ui = QuizInterface(quiz)

off = False
# while quiz.is_still_has_question():
#    quiz.next_question()
#    quiz.checking_answer()