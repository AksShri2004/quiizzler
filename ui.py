from tkinter import *
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"
# user_answer = ""

# class Canvas(Canvas):
#     def __init__(self, quest)
#         super().__init__()



class QuizUI():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # quest = self.get_next_question()

        self.screen = Tk()
        self.screen.title("quizzler")
        self.screen.configure(background=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas()
        self.canvas.configure(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="sss",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(row=2, column=1, columnspan=2,pady=50)

        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")

        self.button_right = Button(image=right, highlightthickness=0, command=self.right)
        self.button_right.grid(row=3, column=1)

        self.button_false = Button(image=wrong, highlightthickness=0, command=self.wrong)
        self.button_false.grid(row=3, column=2)

        self.score_label = Label(text=f"Score: {self.quiz.score}",bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=1, column=2)

        self.get_next_question()
        self.screen.mainloop()


    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def get_next_question(self):
        self.score_label.configure(text=f"Score: {self.quiz.score}")
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="THE enD")
            self.button_right.config(state="disabled")
            self.button_false.config(state="disabled")

    def give_feedback(self, user):
        if user:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.screen.after(1000,self.get_next_question)
