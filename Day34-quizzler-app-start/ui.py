from tkinter import *

from PIL import ImageTk, Image

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = ImageTk.PhotoImage(Image.open("images/true.png"))
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = ImageTk.PhotoImage(Image.open("images/false.png"))
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)









# from tkinter import *
# from PIL import ImageTk, Image
# from functools import partial
# from quiz_brain import QuizBrain
#
#
# THEME_COLOR = "#375362"
#
#
# class QuizInterface:
#     def __init__(self, quiz_brain):
#         self.quiz_brain = quiz_brain
#         self.score = 0
#         self.window = Tk()
#         self.window.title("QuizzGames")
#         self.window.config(padx=20, pady=20, bg=THEME_COLOR)
#
#         self.label_score = Label(text=f"Score: {self.score}")
#         self.label_score.grid(row=0, column=1)
#
#         self.canvas = Canvas(self.window, width=300, height=250)#, font=('Arial', 20, 'italic')
#         self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
#         self.question_text = self.canvas.create_text(
#             150,125,
#             width=280,
#             text="Title", font=('Arial', 20, 'italic'))
#
#
#         img_true = ImageTk.PhotoImage(Image.open("images/true.png"))
#         check_answer_with_args = partial(self.check_answer, 'True')
#         btn_true = Button(image=img_true, highlightthickness=0, command=check_answer_with_args)
#         btn_true.grid(row=2, column=0)
#
#         img_false = ImageTk.PhotoImage(Image.open("images/false.png"))
#         check_answer_with_args1 = partial(self.check_answer, 'False')
#         btn_false = Button(image=img_false, command=check_answer_with_args1)
#         btn_false.grid(row=2, column=1)
#
#         self.get_next_question()
#         self.window.mainloop()
#
#     def get_next_question(self):
#         self.canvas.config(bg='white')
#         question_text = self.quiz_brain.next_question()
#         self.canvas.itemconfig(self.question_text, text=question_text)
#
#     def get_feedback(self, result):
#         if result:
#             self.canvas.config(bg="green")
#             # print('into')
#         else:
#             self.canvas.config(bg="red")
#         self.canvas.after(3000, func=self.get_next_question())
#
#     def check_answer(self, user_choice):
#         if self.quiz_brain.check_answer(user_choice):
#             self.score += 1
#             self.label_score.config(text=f"Score: {self.score}")
#             self.get_feedback(True)
#         else:
#             self.get_feedback(False)