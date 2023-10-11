from tkinter import *
from  quize_brain import QuizeBrain
THEM_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz: QuizeBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEM_COLOR)

        self.label_score = Label(text="Score: 0",bg=THEM_COLOR,fg="white")
        self.label_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300,height=250,)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.text = self.canvas.create_text(150,125, font=("Arial",20,"italic"),fill=THEM_COLOR,text="somthing",width=280)

        self.right_path = PhotoImage(file="images/right.png")
        self.right_button = Button(image=self.right_path,command=self.true)
        self.right_button.grid(column=0,row=2)

        self.wrong_path = PhotoImage(file="images/wrong.png")
        self.wrong_button = Button(image=self.wrong_path,highlightthickness=0,command=self.false)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.is_still_has_question():
            self.label_score.config(text=f"score: {self.quiz.secor}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text,text= q_text)
        else:
            self.canvas.itemconfig(self.text,text="End")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def true(self):
        self.give_feedback(self.quiz.checking_answer("True"))
    def false(self):
        self.give_feedback(self.quiz.checking_answer("False"))



    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)