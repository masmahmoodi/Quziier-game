import html
class  QuizeBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.secor = 0

    def is_still_has_question(self):
        if len(self.question_list)>self.question_number:
            return True
        else:
            return False

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number +=1
        q_text = html.unescape(self.current_question.text)
        return f"  Q{self.question_number}: {q_text}"
        # user_input =  input(f"  Q{self.question_number}: {q_text} (true/false)? ").lower()
        # self.checking_answer(user_input)


    def checking_answer(self,user_input):
        if self.current_question.answer.lower() == user_input.lower():
            self.secor +=1
            return True
        else:
         return False



